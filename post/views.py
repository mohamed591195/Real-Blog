from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import CreatePostForm


@login_required
def home(request):
    posts = Post.pub_posts.all()

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