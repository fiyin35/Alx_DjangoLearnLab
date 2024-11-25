from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns = [
    path('books/', BookList.as_view(), name="book-list"),
    path('token/', obtain_auth_token, name="api_token"),
    # this include all routes registered with the router
    path('', include(router.urls))
]