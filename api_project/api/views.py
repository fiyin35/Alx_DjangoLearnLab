from .models import Book 
from .serializers import BookSerializer
# from rest_framework.generics import ListAPIView
# from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets

from rest_framework import generics
# from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieves all Book instances
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]



