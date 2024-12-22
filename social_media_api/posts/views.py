from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Comment, Post, Like
from .serializers import CommentSerializer, PostSerializer
from notifications.models import Notification

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view, obj):
        # safe methods are allowed for all users
        if request.method in permissions.SAFE_METHODS:
            return True
        # only the object author can edit/delete
        return obj.author == request.user 

# Comments views here.
class CommentViewSets(viewsets.ModelViewSet):
    model = Comment.objects.all()
    authentication_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    serializer_class = CommentSerializer

    def saveComment(self, serializer):
        # set the author of the post to logged in user
        serializer.save(author = self.request.user)





# Posts views here
class PostViewSets(viewsets.ModelViewSet):
    model = Post.objects.all()
    authentication_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    serializer_class = PostSerializer

    def savePost(self, serializer):
        # set the author of the post to the logged user
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


    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except post.DoesNotExist:
            return Response({'detail': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        # check if the user like the post 
        like, created = Like.objects.get_or_created(user=request.user, post=post)

        if not created:
            return Response({'detail': 'You already liked this post'}, status=status.HTTP_400_BAD_REQUEST)
        
        # create a notification for the author
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

    def delete(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({'detail':'post not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # remove the like if already exist
        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response({'detail': 'you have not liked this post yet'}, status=status.HTTP_400_BAD_REQUEST)
        
        like.delete()

        return Response({'detail': 'post unliked successfully'}, status=status.HTTP_204_NO_CONTENT)



