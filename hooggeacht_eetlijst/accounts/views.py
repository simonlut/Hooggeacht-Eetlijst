from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from accounts.forms import ProfileForm, UserForm, AttachmentForm
from accounts.models import Profile, Attachment

from django.contrib.auth.decorators import login_required
from django.db import transaction

from django.shortcuts import render, redirect
from django.contrib import messages

class SignUp(CreateView):
    form_class = UserForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('profile_succes')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

class AttachmentCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'accounts/attachment_detail.html'

    form_class = AttachmentForm

    model = Attachment

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AttachmentCreateView, self).form_valid(form)

class AttachmentListView(ListView):
    model = Attachment

class AttachmentDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    redirect_field_name = 'accounts/attachment_detail.html'

    model = Attachment

class AttachmentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'accounts/account_detail.html'

    form_class = AttachmentForm

    model = Attachment

class AttachmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Attachment
    success_url = reverse_lazy('home')
