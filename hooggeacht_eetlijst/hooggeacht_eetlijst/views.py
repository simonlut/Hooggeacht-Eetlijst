from django.views.generic import TemplateView, CreateView, FormView
from posts.models import PostEater
from posts.views import PostEaterCreateView
from posts.forms import PostEaterForm

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['posteater_form'] = PostEater.objects.all()
        return context


class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class ProfileSucces(TemplateView):
    template_name = 'profile_succes.html'

class Development(TemplateView):
    template_name = 'development.html'
