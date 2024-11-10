from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book


# Create your views here.
def book_list(request):
    """lists all books stored in the database"""
    books = Book.objects.all()
    context = {'list_book': books}
    return render(request, 'relationship_app/list_books.html', context)

class BookDetail(DetailView):
     """A class-based view for displaying details for a specific library"""
     model = Library
     template_name = 'relationship_app/library_detail.html'
     
     def get_context(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['books'] = Book.objects.all()
          return context
          
