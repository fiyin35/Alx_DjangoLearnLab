from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer

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
    model = Comment.objects.all()
    authentication_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    serializer_class = PostSerializer

    def savePost(self, serializer):
        # set the author of the post to the logged user
        serializer.save(author=self.request.user)
