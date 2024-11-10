from django.url import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import book_list, LibraryDetailView, Registation, Login

urlpatterns = [
    path('list-book/', book_list),
    path('library-detail/', LibraryDetailView),
    path('register/', 'views.register', Registation),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout')
]