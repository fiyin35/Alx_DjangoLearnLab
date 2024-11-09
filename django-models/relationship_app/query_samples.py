# relationship_app/query_samples.py

from django.shortcuts import get_object_or_404
from relationship_app.models import Book, Author, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books:
        print(f"- {book.title}")
    return books

def list_all_books_in_library(library_name):
    """List all books in a specific library."""
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Many-to-Many relationship
    print(f"Books in {library.name} Library:")
    for book in books:
        print(f"- {book.title} by {book.author.name}")
    return books
    

def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a specific library."""
    library = Librarian.objects.get(library=library_name)
    librarian = library.librarian  # ForeignKey relationship
    print(f"The librarian for {library.name} Library is {librarian.name}")
    return librarian

