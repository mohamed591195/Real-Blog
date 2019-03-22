from .models import Post, Comment, CommentReply
from django import forms

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['title', 'body', 'image', 'status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
    
class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = ['body']