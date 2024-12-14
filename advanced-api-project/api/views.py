from .models import Book
from .filter import BookFilter
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# from django_filters import rest_framework as filters 


# class BookFilter(filters.FilterSet):
#     title = filters.CharFilter(lookup_expr='icontains')  # Allows case-insensitive partial matches
#     author = filters.CharFilter(field_name='author__name', lookup_expr='icontains')
#     publication_year = filters.NumberFilter()

#     class Meta:
#         model = Book
#         fields = ['title', 'author', 'publication_year']


# Create your views here.
class BookListView(generics.ListAPIView):
    '''retrieve all the books stored in the database'''
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title', 'publication_year']  # Specify ordering fields
    ordering = ['title']  # Default ordering (optional)
    filterset_class = BookFilter
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

class CreateAuthorView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = AuthorSerializer



class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    '''Delete a book from the database'''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

