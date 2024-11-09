# relationship_app/query_samples.py

from django.shortcuts import get_object_or_404
from relationship_app.models import Book, Author, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    author = get_object_or_404(Author, name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
   

def list_all_books_in_library(library_name):
    """List all books in a specific library."""
    library = get_object_or_404(Library, name=library_name)
    books = library.books.all()  # Many-to-Many relationship
    print(f"Books in {library.name} Library:")
    

def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a specific library."""
    library = get_object_or_404(Library, name=library_name)
    librarian = library.librarian  # ForeignKey relationship
    print(f"The librarian for {library.name} Library is {librarian.name}")
    return librarian

