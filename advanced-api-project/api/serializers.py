from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        field = ['author']