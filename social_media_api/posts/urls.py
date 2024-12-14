from .views import CommentViewSets, PostViewSets
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register(r'posts', PostViewSets, basename='posts')
router.register(r'comments', CommentViewSets, basename='comments')

urlpatterns = [
    path('', include(router.urls))
]