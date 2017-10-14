from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from accounts.forms import ProfileForm
from accounts.models import Profile

class AccountSettings(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'home'

    form_class = ProfileForm

    model = Profile

    template_name = "accounts/account_settings.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ProfileForm, self).form_valid(form)
