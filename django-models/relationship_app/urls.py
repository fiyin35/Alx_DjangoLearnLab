from django.url import path
from . import views

urlpatterns = [
    path('list-book', views.book_list),
    path('library-detail', views.BookDetail)
]