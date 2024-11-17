from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

# Create your views here.
def book_list(request):
    """lists all books stored in the database"""
    books = Book.objects.all()
    context = {'list_book': books}
    return render(request, 'relationship_app/list_books.html', context)

@permission_required('bookshelf.can_create', raise_exception=True)
def createBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-book')
    else:
        form = BookForm()
    return render(request, 'bookshelf/add_book.html', {'book': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def editBook(request, book_id):
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
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_view', raise_exception=True)
def viewBook(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def deleteBook(request, book_id):
    book = Book.get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('list-book')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

