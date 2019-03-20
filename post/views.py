from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Post


def home(request):
    posts = Post.pub_posts.all()

    return render(request, 'post/home.html', {'posts': posts})

def DetailView(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'post/detail.html', {'post': post})