from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eat_time = #
    attachment_eater = models.ForeignKey(attachment_profile)
    extra_eaters = models.PositiveSmallIntegerField()
    extra_eater_veg = #Number slider
    extra_eater_allergy = models.CharField(max_length=124, blank=True)
    submit_time =

class ExtraEaterPreference(modes.Model):
    extra_eater = models.ForeignKey(Post, on_delete=models.CASCADE)
    vegetarian =  models.BooleanField(blank = True)
    allergy = models.CharField(max_length=30, blank=True)
