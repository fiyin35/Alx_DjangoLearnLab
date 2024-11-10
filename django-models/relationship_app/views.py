from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


# Create your views here.
def book_list(request):
    """lists all books stored in the database"""
    books = Book.objects.all()
    context = {'list_book': books}
    return render(request, 'books/list_books.html', context)

class BookDetail(DetailView):
     """A class-based view for displaying details for a specific library"""
     model = Library
     template_name = 'relationship_app/list_books.html'
     
     def get_context(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['books'] = Book.objects.all()
          return context
          
