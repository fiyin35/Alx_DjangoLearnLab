from django.url import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('list-book', list_books),
    path('library-detail', LibraryDetailView)
]