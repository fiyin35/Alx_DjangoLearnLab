from .models import Comment, Post
from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    author = serializers.StringRelatedField()

    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all)
    class Meta:
        model = Comment
        fields = ['post', 'author', 'content', 'created_at', 'updated_at']



class PostSerializer(serializers.Serializer):
    # Including the author's username and email for easy representation
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'created_at', 'updated_at']
