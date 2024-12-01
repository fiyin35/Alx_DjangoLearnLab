from rest_framework import serializers
from .models import Book, Author
import datetime


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # function to validate the publication year to ensure it's not above the current year
    # which means publication_year can not be set to future date
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year

        if value > current_year:
            serializers.ValidationError("Publication year can not be in the future")
        
        return value


class AuthorSerializer(serializers.ModelSerializer):

    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']