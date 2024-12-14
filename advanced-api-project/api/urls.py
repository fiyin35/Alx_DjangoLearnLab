from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from .views import CreateAuthorView
from rest_framework.authtoken.views import obtain_auth_token


# router = DefaultRouter()


urlpatterns = [
    path('books/', BookListView.as_view(), name="book-list"), # endpoint url to list all the books in the DB
    path('books/<int:pk>/', BookDetailView.as_view(), name="book-detail"), # endpoint url to show details of each book, using the book id
    path('books/create/', BookCreateView.as_view(), name="create-book"), # endpoint url to create a new book, POST request
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name="update-book"), # endpoint url to update a book using the id, PUT/PATCH request
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name="delete-book"), # endpoint url to delete a book using the book id
    path('books/create-author/', CreateAuthorView.as_view(), name="create-author"), # endpoint to create author in the db
    path('token/', obtain_auth_token, name="api_token"),

]