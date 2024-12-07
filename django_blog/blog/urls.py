from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Registration, profile, post_search, PostByTagListView
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
from .views import CommentCreateView, CommentDeleteView, CommentUpdateView


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
    path('post/<int:pk>/comments/new/', CommentCreateView, name='comment_create'), # to create new comment in post detail
    path('comment/<int:pk>/update/', CommentUpdateView, name='comment_edit'), # to update a comment
    path('comment/<int:pk>/delete/', CommentDeleteView, name='comment_delete'), # to delete a comment
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post_tags'),
    path('search/', post_search, name='search'),
]
