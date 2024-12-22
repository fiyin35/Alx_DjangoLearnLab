from .views import CommentViewSets, PostViewSets, FeedView, LikePostView, UnlikePostView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register(r'posts', PostViewSets, basename='posts')
router.register(r'comments', CommentViewSets, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike')
]