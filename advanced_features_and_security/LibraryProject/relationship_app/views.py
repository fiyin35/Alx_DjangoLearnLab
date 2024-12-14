from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Library
from .models import Book
from .models import UserProfile
from .forms import BookForm


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
     
     def register(request):
        form = UserCreationForm() if request.method == "GET" else UserCreationForm(request.POST)
        # Handle form submission
        if request.method == "POST" and form.is_valid():
            user = form.save()
            login(request, user)  # Log in the new user automatically after registration
            return redirect(reverse_lazy('login'))  # Redirect to login page
        return render(request, 'relationship_app/register.html', {'form': form})
         
     
         

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

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-book')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'book': book})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book_view(request, book_id):
    """get the book instance to edit using book id"""
    book = Book.get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=request.book)
        if form.is_valid():
            form.save()
            redirect('list-book')
    else:
        """initialize the form with the current book instance for GET request"""
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book_view(request, book_id):
    book = Book.get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('list-book')
    return render(request, 'relationship_app/delete_book.html', {'book': book})





          
