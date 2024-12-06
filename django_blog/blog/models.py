from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.TextField(blank=True, null=True, max_length=35, unique=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


