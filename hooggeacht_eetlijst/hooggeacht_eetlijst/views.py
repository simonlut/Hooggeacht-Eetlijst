from django.views.generic import TemplateView, CreateView, FormView
from posts.models import PostEater, PostCook
from posts.views import PostEaterCreateView
from posts.forms import PostEaterForm
from django.utils import timezone
from datetime import date


class Intro(TemplateView):
    template_name = 'intro.html'

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['postcook_list'] = PostCook.objects.filter(submit_time__date=date.today()).order_by('-submit_time')
        context['posteater_list'] = PostEater.objects.filter(submit_time__date=date.today()).order_by('-submit_time')
        # context['posteater_template'] = PostEater.objects.order_by('submit_time')
        return context

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class ProfileSucces(TemplateView):
    template_name = 'profile_succes.html'

class Development(TemplateView):
    template_name = 'development.html'
