from django.url import path
from .views import book_list, LibraryDetailView, Registation
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('list-book/', book_list),
    path('library-detail/', LibraryDetailView),
    path('register/', 'views.register', Registation),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name="logout")
]