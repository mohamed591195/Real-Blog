from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.home, name='home-page'),
    path('post/<slug:slug>/<int:year>/<int:month>/<int:day>', views.DetailView, name='post-page'),
    path('createpost', views.CreatePostView, name='createpost-page'),
    path('<slug:blogger>/myposts', views.MyPostsView, name='myposts-page'),
    path('<slug:slug>/<int:year>/<int:month>/<int:day>/edit', views.UpdatePostView, name='updatepost-page'),
    path('delete/<int:id>', views.DeleteView, name='delete-page')
]