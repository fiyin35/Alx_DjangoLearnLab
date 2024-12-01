from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


# Create your views here.
class BookListView(generics.ListAPIView):
    '''retrieve all the books stored in the database'''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [IsAuthenticated]
    permission_classes = [TokenAuthentication]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [IsAuthenticated]
    permission_classes = [TokenAuthentication]

class BookDeleteView(generics.DestroyAPIView):
    '''Delete a book from the database'''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [IsAuthenticated]
    permission_classes = [TokenAuthentication]