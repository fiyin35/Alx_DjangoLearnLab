from django.urls import path
from django.contrib.auth import views
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView


urlpattern = [
    path('books/', ListView.as_view()),
    path('books/<int:pk>/', DetailView),
    path('books/create/', CreateView),
    path('books/update/', UpdateView),
    path('books/delete/', DeleteView)
]