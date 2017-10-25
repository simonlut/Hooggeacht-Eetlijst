from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    housename = models.CharField(max_length=30, blank=True)
    vegetarian = models.NullBooleanField(blank=True, null=True)
    allergy = models.CharField(max_length=100, blank=True, null=True)
    food_preference = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Attachment(models.Model):
    attachment = models.ForeignKey(User, on_delete=models.CASCADE)
    at_img = models.ImageField()
    at_first_name = models.CharField(max_length=30, blank=True)
    at_last_name = models.CharField(max_length=30, blank=True)
    at_veg = models.NullBooleanField(blank=True, null=True)
    at_allergy = models.CharField(max_length=100, blank=True, null=True)
