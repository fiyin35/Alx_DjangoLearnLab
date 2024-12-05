from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Registration, profile
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('register/',  Registration.as_view(), name="register"),
    path('profile/', profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/new', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='update_post'),
    path('post/<>int:pk/', PostDetailView.as_view(), name='update_post'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='delete_post')
]
