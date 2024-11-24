from .models import Book 
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()  # Retrieves all Book instances
    serializer_class = BookSerializer