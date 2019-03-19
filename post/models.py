from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify
def custom_slugify(value):
    return default_slugify(value).replace(' ', '-')

class Profile(models.Model):
    SEX_CHOICES = (('M', 'Male'), ('F', 'Female'))
    first_name = models.CharField('First Name', max_length=20, blank=True)
    second_name = models.CharField('First Name', max_length=20, blank=True)
    image = models.ImageField('Personal Image', upload_to='post/profile/', default='media/blog/profile.jpg')
    email = models.EmailField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(choices=SEX_CHOICES, max_length=20, blank=True)

    def save(self, *args, **kwargs):
        self.first_name = self.user.first_name
        self.second_name = self.user.second_name
        self.email = self.user.email
        super().save(*args, **kwargs)

class Author(models.Model):
    bio = models.TextField('description (bio)', blank=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile.first_name} {self.profile.second_name}'

class Post(models.Model):
    STATUS_CHOICES = (('p', 'Published'), ('d', 'Draft'))
    title = models.CharField('post title', max_length=50)
    slug = AutoSlugField(populate_from='title', unique_for_date='created', slugify=custom_slugify)
    body = models.TextField('post body')
    image = models.ImageField('post image', upload_to='post/posts/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField( 'post status', max_length=50, choices=STATUS_CHOICES)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    
    class Meta:
        ordering = ['-published']
    
    def get_absolute_url(self):
        pass
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return f'comment on{self.post}'

class CommentReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
    body = models.TextField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    
    def __str__(self):
        return f'reply on {self.comment} of {self.comment.post}'