from django.contrib.auth import get_user_model
from posts.models import PostEater, PostCook
from django import forms

class PostEaterForm(forms.ModelForm):
    class Meta:
        fields = ('eat','extra_eaters','attachment_eater','extra_eater_veg', 'extra_eater_allergy')
        model = PostEater


class PostCookForm(forms.ModelForm):
    class Meta:
        fields = ('extra_eaters', 'extra_eater_veg', 'extra_eater_allergy')
        model = PostCook
