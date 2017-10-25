from django.contrib.auth import get_user_model
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ('vegetarian', 'allergy', 'food_preference')
        model = Profile

class UserForm(UserCreationForm):
    class Meta:
        fields = ('email','password1','password2','username',)
        model = get_user_model()
    # 
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['username'].label = ''
    #     self.fields['email'].label = ""
    #     self.fields['password1'].label = ""
    #     self.fields['password2'].label = ""
    #     self.fields['username'].help_text =''
    #     self.fields['email'].help_text = ""
    #     self.fields['password1'].help_text = ""
    #     self.fields['password2'].help_text = ""
