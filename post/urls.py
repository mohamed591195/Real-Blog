from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.home, name='home-page'),
    path('post/<slug:slug>/<int:year>/<int:month>/<int:day>', views.DetailView, name='post-page'),
    path('createpost', views.CreatePostView, name='createpost-page')
]