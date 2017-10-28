from django.db import models

# Create your models here.
class PostEater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attachment_eater = models.ForeignKey(attachment_profile, blank=True)
    extra_eaters = models.PositiveSmallIntegerField(blank=True)
    extra_eater_veg = models.PositiveSmallIntegerField(blank=True) #Number slider
    extra_eater_allergy = models.CharField(max_length=124, blank=True)
    submit_time = models.DateTimeField(auto_now_add=True)

class PostCook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eat_time = models.DateField() #standaard half 6
    food = models.CharField(max_length=30, blank=True)
    extra_eaters = models.PositiveSmallIntegerField(blank=True)
    extra_eater_veg = models.PositiveSmallIntegerField(blank=True) #Number slider
    extra_eater_allergy = models.CharField(max_length=124, blank=True)
    submit_time = models.DateTimeField(auto_now_add=True)
