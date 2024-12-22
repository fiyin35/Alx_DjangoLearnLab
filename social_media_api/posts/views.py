from rest_framework import generics  # Use DRF's version of get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment, Post, Like
from .serializers import CommentSerializer, PostSerializer
from notifications.models import Notification

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view, obj):
        # Safe methods are allowed for all users
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only the object author can edit/delete
        return obj.author == request.user 

# Comments views here.
class CommentViewSets(viewsets.ModelViewSet):
    queryset = Comment.objects.all()  # Use `queryset` instead of `model`
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        # Set the author of the comment to the logged-in user
        serializer.save(author=self.request.user)

# Posts views here
class PostViewSets(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # Use `queryset` instead of `model`
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        # Set the author of the post to the logged-in user
        serializer.save(author=self.request.user)

# Feeds 
class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Get the post or return a 404 error
        post = generics.get_object_or_404(Post, pk=pk)
        
        # Check if the user has already liked the post
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({'detail': 'You already liked this post'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a notification for the author
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='Liked',
                target=post
            )

        return Response({'detail': 'Post liked successfully'}, status=status.HTTP_201_CREATED)
    
class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        # Get the post or return a 404 error
        post = generics.get_object_or_404(Post, pk=pk)
        
        # Remove the like if it exists
        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response({'detail': 'You have not liked this post yet'}, status=status.HTTP_400_BAD_REQUEST)
        
        like.delete()

        return Response({'detail': 'Post unliked successfully'}, status=status.HTTP_204_NO_CONTENT)
