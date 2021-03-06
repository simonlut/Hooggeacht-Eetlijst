from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


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

user = get_user_model()

class Attachment(models.Model):
    author = models.ForeignKey(user)
    # at_img = models.ImageField()
    at_first_name = models.CharField(max_length=30, blank=True)
    at_last_name = models.CharField(max_length=30, blank=True)
    at_veg = models.NullBooleanField(blank=True, null=True)
    at_allergy = models.CharField(max_length=100, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("accounts:attachment_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.at_first_name
