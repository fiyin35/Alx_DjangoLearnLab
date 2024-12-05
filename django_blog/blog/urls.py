from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Registration, profile


urlpatterns = [
    #path('/', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name="login"),
    path('register/',  Registration.as_view(), name="register"),
    path('profile/', profile, name="profile"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name="logout")
    # path('profile/')
]
