from django.urls import path
from .views import RegisterView, UpdateProfileView, BeAuthorView
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'users'
urlpatterns = [
    path('register/',RegisterView, name='register-page'),
    path('login/', LoginView.as_view(template_name='users/login.html') , name='login-page'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout-page'),
    path('profile', UpdateProfileView, name='profile-page'),
    path('be-author', BeAuthorView, name='beauthor-page')
]