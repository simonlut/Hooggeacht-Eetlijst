from django.conf.urls import url
from django.contrib.auth import views as auth_views
from posts import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'posts'

urlpatterns = [
    url(r'^inschrijven/$',views.PostEaterCreateView.as_view(), name="posteater_create"),
    url(r'^inschrijven/list/$', views.PostEaterListView.as_view(), name="posteater_list"),
    url(r'^inschrijven/(?P<pk>\d+)$', views.PostEaterDetailView.as_view(), name="posteater_detail"),
    url(r'^inschrijven/(?P<pk>\d+)/aanpassen/$', views.PostEaterUpdateView.as_view(), name="posteater_update"),
    url(r'^inschrijven/(?P<pk>\d+)/verwijder/$', views.PostEaterDeleteView.as_view(), name="posteater_delete"),
]
