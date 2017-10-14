from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    vegetarian = models.BooleanField(blank=True)
    allergy = models.CharField(max_length=100, blank=True)
    food_preference = models.CharField(max_length=100, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
