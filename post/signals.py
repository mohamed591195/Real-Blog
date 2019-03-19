from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def CreateAuthor(sender,instance, created, **kwargs):
    print(kwargs)
    if created:
        new_profile = Profile( user=instance)
        new_profile.save()
