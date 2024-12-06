from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Registration, profile
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
from .views import CommentCreateView, CommentDeleteView, CommentUpdateView, CommentViewAll


urlpatterns = [
    path('', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('register/',  Registration.as_view(), name="register"),
    path('profile/', profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<>int:pk/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('comments/<int:pk>/new/', CommentCreateView.as_view(), name='comment_create'), # to create new comment in post detail
    path('comments/', CommentViewAll.as_view(), name='comment_all'), # to view all comments
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_update'), # to update a comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'), # to delete a comment
]
