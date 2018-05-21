from django.contrib import auth
from django.db import models
from django.utils import timezone
from datetime import date, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from accounts.models import Attachment
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from schedule.models import Event, EventRelation, Calendar

# from posts.models import PostCook



# Create your models here.
class PostEater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eat = models.BooleanField(default=True)
    attachment_eater = models.ForeignKey(Attachment, default=1,blank=True, null=True)
    extra_eaters = models.PositiveSmallIntegerField(default=0,blank=True)
    extra_eater_veg = models.PositiveSmallIntegerField(default=0,blank=True) #Number slider
    extra_eater_allergy = models.CharField(default=0,max_length=124, blank=True)
    submit_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=30 , blank=True)
    startDateTime = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("home")

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
    eat_time = models.TimeField(auto_now=False,default="18:30") #standaard half 6
    food = models.CharField(max_length=30, blank=True)
    extra_eaters = models.PositiveSmallIntegerField(default=0,blank=True)
    extra_eater_veg = models.PositiveSmallIntegerField(default=0,blank=True) #Number slider
    extra_eater_allergy = models.CharField(default=0,max_length=124, blank=True)
    description = models.CharField(max_length=30 , blank=True)
    startDateTime = models.DateTimeField(auto_now=True)
    submit_time = models.DateTimeField(auto_now=True)
    eater = models.OneToOneField(
            PostEater,
            on_delete=models.CASCADE,
            primary_key=True,
            default=1,
        )

    def get_absolute_url(self):
        return reverse("home")

    def __str__(self):
        return self.user.username + str(self.submit_time)


    #
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

    def save(self, force_insert=False, force_update=False):
        new_task = True
        super(PostCook, self).save(force_insert, force_update)
        end = self.startDateTime + timedelta(minutes=1)
        description = "http://127.0.0.1:8000/posts/"+str(self.submit_time.strftime("%Y/%b/%d"))
        if new_task:
            event = Event(start=self.startDateTime, end=end, title=self.user,
                      description=description, calendar_id=1)
            event.save()
            rel = EventRelation.objects.create_relation(event, self)
            rel.save()
            try:
                cal = Calendar.objects.get(name="hooggeacht")
            except Calendar.DoesNotExist:
                cal = Calendar(name="bla")
                cal.save()
            cal.events.add(event)
        else:
            event = Event.objects.get_for_object(self)[0]
            event.start = self.startDateTime
            event.end = end
            event.title = title
            event.description = self.description
            event.save()
