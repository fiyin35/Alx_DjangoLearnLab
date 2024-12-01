from django_filters import rest_framework as filters 
from .models import Book


class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')  # Allows case-insensitive partial matches
    author = filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    publication_year = filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']