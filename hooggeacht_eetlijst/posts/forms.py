from django.contrib.auth import get_user_model
from posts.models import PostEater, PostCook
from schedule.models.events import Event
from django import forms
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class PostEaterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user')
         super(PostEaterForm, self).__init__(*args, **kwargs)

    class Meta:
        fields = ('eat','extra_eaters','attachment_eater','extra_eater_veg', 'extra_eater_allergy')
        model = PostEater

    def clean(self):
        submit_time = self.cleaned_data.get('submit_time')
        if PostEater.objects.filter(user=self.user,submit_time__date=date.today()).exists():
            raise ValidationError(_("Ja je staat al op eten mongool."))
        qs = PostCook.objects.filter(user=self.user,submit_time__date=date.today())
        if qs.exists():
            qs.delete()


class PostCookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user')
         super(PostCookForm, self).__init__(*args, **kwargs)

    class Meta:
        fields = ('extra_eaters', 'extra_eater_veg', 'extra_eater_allergy')
        model = PostCook

    def clean(self):
        submit_time = self.cleaned_data.get('submit_time')
        if PostCook.objects.filter(user=self.user,submit_time__date=date.today()).exists():
            raise ValidationError(_("Ja je staat al op koken mongool."))
        qs = PostEater.objects.filter(user=self.user,submit_time__date=date.today())
        if qs.exists():
            qs.delete()
