from django.contrib import auth
from django.db import models
from django.utils import timezone
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from accounts.models import Attachment
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
# from posts.models import PostCook



# Create your models here.
class PostEater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eat = models.BooleanField(default=True)
    attachment_eater = models.ForeignKey(Attachment, default=1,blank=True, null=True)
    extra_eaters = models.PositiveSmallIntegerField(default=0,blank=True)
    extra_eater_veg = models.PositiveSmallIntegerField(default=0,blank=True) #Number slider
    extra_eater_allergy = models.CharField(default=0,max_length=124, blank=True)
    submit_time = models.DateTimeField()

    def save(self, *args, **kwargs):
            ''' On save, update timestamps '''
            if not self.id:
                self.submit_time = timezone.now()
            return super(PostEater, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:posteater_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.user.username + str(self.submit_time)

    # def clean(self):
    #     # Don't allow draft entries to have a pub_date.
    #     if self.extra_eaters < self.extra_eater_veg:
    #         raise ValidationError(_('He man, leer is rekenen, hoe kun je nou meer extra veggies hebben dan het totaal aantal extra mensen.'))
    #
    # def validate_unique(self, exclude=None):
    #     qs = PostEater.objects.filter(submit_time__date=date.today())
    #     # if f.exists():
    #     #     raise ValidationError(_('WEJOW BITCHES'))
    #     if qs.exists():
    #         raise ValidationError(_('Je hebt je al ingeschreven voor vandaag.'))
    #     s = PostCook.objects.filter(submit_time__date=date.today())
    #     if s.exists():
    #         s.delete()

class PostCook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # eat_time = models.TimeField() #standaard half 6
    # food = models.CharField(max_length=30, blank=True)
    extra_eaters = models.PositiveSmallIntegerField(default=0,blank=True)
    extra_eater_veg = models.PositiveSmallIntegerField(default=0,blank=True) #Number slider
    extra_eater_allergy = models.CharField(default=0,max_length=124, blank=True)
    submit_time = models.DateTimeField()
    eater = models.OneToOneField(
            PostEater,
            on_delete=models.CASCADE,
            primary_key=True,
            default=1,
        )

    def get_absolute_url(self):
        return reverse("posts:postcook_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.user.username + str(self.submit_time)


    def save(self, *args, **kwargs):
            ''' On save, update timestamps '''
            self.submit_time = timezone.now()
            return super(PostCook, self).save(*args, **kwargs)

    # def validate_unique(self, exclude=None):
    #     qs = PostCook.objects.filter(submit_time__date=date.today())
    #     if qs.exists():
    #         raise ValidationError('Je staat al op koken.')
    #     s = PostEater.objects.filter(submit_time__date=date.today())
    #     if s.exists():
    #             s.delete()
