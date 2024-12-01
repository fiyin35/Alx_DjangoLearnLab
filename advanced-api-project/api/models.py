from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=80)
    publication_year = models.IntegerField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
