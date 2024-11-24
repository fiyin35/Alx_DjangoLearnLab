from .models import Book 
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView
import rest_framework 

# Create your views here.
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieves all Book instances
    serializer_class = BookSerializer