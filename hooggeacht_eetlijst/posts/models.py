from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eat_time = models.DateField()#
    attachment_eater = models.ForeignKey(attachment_profile)
    extra_eaters = models.PositiveSmallIntegerField()
    extra_eater_veg = models.PositiveSmallIntegerField() #Number slider
    extra_eater_allergy = models.CharField(max_length=124, blank=True)
    submit_time = models.DateTimeField(auto_now_add=True)
