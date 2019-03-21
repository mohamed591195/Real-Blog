from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Author


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('the email is already exist')
        return email
    
class ProfileForm(forms.ModelForm): 
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image', 'sex']
    
class BeAuthorForm(forms.ModelForm):
    class Meta:
        model= Author
        fields = ['bio']