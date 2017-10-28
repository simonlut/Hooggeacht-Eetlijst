from django.contrib.auth import get_user_model
from posts.models import PostEater, PostCook
from django import forms

class PostEaterForm(forms.ModelForm):
    class Meta:
        fields = ('attachment_eater', 'extra_eaters', 'extra_eater_veg', 'extra_eater_allergy')
        model = PostEater

class PostCookForm(forms.ModelForm):
    class Meta:
        field = ('eat_time','attachment_eater', 'extra_eaters', 'extra_eater_veg', 'extra_eater_allergy')
        model = PostCook
