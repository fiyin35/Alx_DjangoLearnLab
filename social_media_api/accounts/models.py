from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.TextField(max_length=50, null=False, blank=False)
    bio = models.TextField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False)

    def __self__(self):
        return self.bio

