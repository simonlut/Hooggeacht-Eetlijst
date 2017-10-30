from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


# Create your models here.
class PostEater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # attachment_eater = models.ForeignKey(attachment_profile, blank=True)
    extra_eaters = models.PositiveSmallIntegerField(blank=True)
    extra_eater_veg = models.PositiveSmallIntegerField(blank=True) #Number slider
    extra_eater_allergy = models.CharField(max_length=124, blank=True)
    submit_time = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("posts:posteater_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.user.username

class PostCook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eat_time = models.DateField() #standaard half 6
    food = models.CharField(max_length=30, blank=True)
    extra_eaters = models.PositiveSmallIntegerField(blank=True)
    extra_eater_veg = models.PositiveSmallIntegerField(blank=True) #Number slider
    extra_eater_allergy = models.CharField(max_length=124, blank=True)
    submit_time = models.DateTimeField(auto_now_add=True)
