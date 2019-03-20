from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def home(request):
    posts = Post.pub_posts.all()

    return render(request, 'post/home.html', {'posts': posts})
@login_required
def DetailView(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'post/detail.html', {'post': post})