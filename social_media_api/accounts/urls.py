from django.contrib import admin
from django.urls import include, path 
from .views import RegistrationView, LoginView, ProfileView



urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
]