from .models import Post
from django import forms

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['title', 'body', 'image', 'status']
