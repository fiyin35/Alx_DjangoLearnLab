from .models import Book 
from .serializers import BookSerializer
import rest_framework

# Create your views here.
class BookList(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer