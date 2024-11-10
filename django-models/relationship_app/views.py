from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Library
from .models import Book
from .models import UserProfile


# Create your views here.
def book_list(request):
    """lists all books stored in the database"""
    books = Book.objects.all()
    context = {'list_book': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
     """A class-based view for displaying details for a specific library"""
     model = Library
     template_name = 'relationship_app/library_detail.html'
     
     def get_context(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['books'] = Book.objects.all()
          return context

class Registation(CreateView):
     form_class = UserCreationForm
     success_url = reverse_lazy('login')
     template_name = 'relationship_app/register.html'

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarians'

@user_passes_test(is_librarian)
def library_view(request):
    return render(request, 'relationship_app/librarian_view.html')

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Members'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



          
