from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, ProfileForm, BeAuthorForm
from django.contrib import messages

# Create your views here.



def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['first_name'] + form.cleaned_data['last_name']
            messages.success(request, f'Account Created succefully {name}')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('users:profile-page')
    else:
        form = RegisterForm()
    
    return render(request, 'users/register.html', {'form': form})


@login_required
def UpdateProfileView(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('post:home-page')
        
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'form': form})


@login_required
def BeAuthorView(request):
    if request.method == 'POST':
        form = BeAuthorForm(request.POST)
        if form.is_valid():
            ins = form.save(commit=False)
            ins.profile = request.user.profile
            ins.save()
            return redirect('post:createpost-page')
    else:
        form = BeAuthorForm()
    
    return render(request, 'users/beauthor.html', {'form': form})