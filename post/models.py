from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify




class Profile(models.Model):
    SEX_CHOICES = (('M', 'Male'), ('F', 'Female'))
    first_name = models.CharField('First Name', max_length=20, blank=True)
    last_name = models.CharField('Last Name', max_length=20, blank=True)
    image = models.ImageField('Personal Image', upload_to='post/profile/', default='media/blog/profile.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(choices=SEX_CHOICES, max_length=20, blank=True)

    def save(self, *args, **kwargs):
        self.first_name = self.user.first_name
        self.last_name = self.user.last_name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name + self.last_name


class Author(models.Model):
    bio = models.TextField('description (bio)', blank=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile.first_name} {self.profile.last_name}'




def custom_slugify(value):
    return default_slugify(value).replace(' ', '-')



class published_posts(models.Manager):
    def get_queryset(self):
        # if super().get_queryset() == None:
        #     super().get_queryset()
        # else:
        return super().get_queryset().filter(status='p')
        
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
    objects = models.Manager()
    pub_posts = published_posts()
    class Meta:
        ordering = ['-published']
    
    def get_absolute_url(self):
        return reverse('post:post-page', kwargs={'slug':self.slug})
    
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







        