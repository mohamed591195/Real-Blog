from django.urls import path
from .views import RegisterView
app_name = 'users'
urlpatterns = [
    path('register',RegisterView, name='registeration-page')
]