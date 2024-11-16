from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(null=False)


    def __str__(self):
        return f"{self.title} by {self.author} published in {self.publication_year}"

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.PhotoField()
