from django.urls import path
from django.contrib.auth import views
from .views import ListView, DetailView, CreateView


urlpattern = [
    path('books/', ListView.as_view()),
    path('books/<int:pk>/', DetailView.as_view()),
    path('books/add/', CreateView.as_view()),
]