from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.views import OwnObjectsMixin

from posts.forms import PostEaterForm, PostCookForm
from posts.models import PostEater, PostCook

from django.contrib.auth.decorators import login_required
from django.db import transaction

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

from django.utils import timezone
from datetime import date




# Create your views here.
class PostEaterCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'posts/posteater_form.html'

    form_class = PostEaterForm

    model = PostEater

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostEaterCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostEaterCreateView, self).get_context_data(**kwargs)
        context['posteater_form'] = PostEater()
        return context


class PostEaterDetailView( LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    redirect_field_name = 'posts/posteater_form.html'

    model = PostEater


class PostEaterUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'posts/posteater_form.html'

    form_class = PostEaterForm

    model = PostEater

class PostEaterDeleteView(LoginRequiredMixin, DeleteView):
    model = PostEater
    success_url = reverse_lazy('home')

class PostEaterListView( LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'posts/posteater_list.html'

    model = PostEater

    def get_queryset(self):
        return PostEater.objects.filter(submit_time__date=date.today())
