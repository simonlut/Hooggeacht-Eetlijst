from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'posts'

urlpatterns = [
    url(r'post/eater')
]
