from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from .forms import CreatePostForm
from django.core.paginator import Paginator


def home(request):
    query_list = Post.pub_posts.all()
    paging = Paginator(query_list, 6)
    page = request.GET.get('page', 1)
    posts = paging.page(page)
    return render(request, 'post/home.html', {'posts': posts})

@login_required
def DetailView(request, slug, year, month, day):
    post = get_object_or_404(Post, slug=slug, 
                                   published__year=year,
                                   published__month=month,
                                   published__day=day )

    return render(request, 'post/detail.html', {'post': post})

@login_required
def CreatePostView(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST,request.FILES)
        if form.is_valid():
            ins = form.save(commit=False)
            ins.author = request.user.profile.author
            ins.save()
            return redirect('post:home-page')
    else:
        form = CreatePostForm()

    return render(request, 'post/createpost.html', {'form': form})


@login_required
def MyPostsView(request, blogger):
    blogger = User.objects.get(username=blogger)
    return render(request, 'post/myposts.html', {'blogger':blogger})

@login_required
def UpdatePostView(request, slug, year, month, day):
    if request.method == 'POST':
        form = CreatePostForm(request.POST,request.FILES, instance=request.user.profile.author.posts.get( slug=slug, 
                                                                                                        published__year=year,
                                                                                                        published__month=month,
                                                                                                        published__day=day))
        if form.is_valid():
            form.save()
            return redirect('post:myposts-page')
    else:
        form = CreatePostForm(instance=request.user.profile.author.posts.get( slug=slug, 
                                                                              published__year=year,
                                                                              published__month=month,
                                                                              published__day=day))

    return render(request, 'post/createpost.html', {'form': form})