from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.

def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    
    return render(request, 'users/register.html', {'form': form})
