from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.home, name='home-page'),
    path('post/<slug:slug>/', views.DetailView, name='post-page')
]