from django.contrib.auth import get_user_model
from django.contrib.auth.forms import User
from accounts.models import Profile
from django import forms



class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ('vegetarian', 'allergy', 'food_preference')
        model = Profile
