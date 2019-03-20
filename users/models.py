from django.db import models
from django.contrib.auth.models import User

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



