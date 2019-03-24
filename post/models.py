from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify
from users.models import Author
from PIL import Image



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
    slug = AutoSlugField(populate_from='title', unique_for_date='published', slugify=custom_slugify)
    body = models.TextField('post body')
    image = models.ImageField('post image', upload_to='post/posts/', blank=True)
    thum_image = models.ImageField('Thumb image', upload_to='post/posts/', blank=True, default='post/posts/default-thumbnail.jpg' )
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField( 'post status', max_length=50, choices=STATUS_CHOICES)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    objects = models.Manager()
    pub_posts = published_posts()
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.thum_image.path)
        output = (300, 174)
        if img.height > 300 and img.width >300:
            img.thumbnail(output)

            img.save(self.thum_image.path)

    class Meta:
        ordering = ['-published']
    
    def get_absolute_url(self):
        return reverse('post:post-page', kwargs={'slug':self.slug,
                                                 'year': self.published.year,
                                                 'month': self.published.month,
                                                 'day': self.published.day})
    def get_update_url(self):
        return reverse('post:updatepost-page', kwargs={'slug':self.slug,
                                                 'year': self.published.year,
                                                 'month': self.published.month,
                                                 'day': self.published.day})
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.body[:20]

class CommentReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
    body = models.TextField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    
    def __str__(self):
        return f'reply on {self.comment} of {self.comment.post}'







        