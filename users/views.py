from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.

def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['first_name'] + form.cleaned_data['last_name']
            messages.success(request, f'Account Created succefully {name}')
            return redirect('post:home-page')
    else:
        form = RegisterForm()
    
    return render(request, 'users/register.html', {'form': form})
