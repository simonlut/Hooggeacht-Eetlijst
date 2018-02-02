from django.conf.urls import url
from django.contrib.auth import views as auth_views
from posts import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'posts'

urlpatterns = [
    url(r'^inschrijven/$',views.PostEaterCreateView.as_view(), name="posteater_create"),
    url(r'^inschrijven/list/$', views.PostEaterListView.as_view(), name="posteater_list"),
    url(r'^inschrijven/future/$', views.PostEaterTemplateView.as_view(), name="posteater_template"),
    url(r'^inschrijven/(?P<pk>\d+)$', views.PostEaterDetailView.as_view(), name="posteater_detail"),
    url(r'^inschrijven/(?P<pk>\d+)/aanpassen/$', views.PostEaterUpdateView.as_view(), name="posteater_update"),
    url(r'^inschrijven/(?P<pk>\d+)/verwijder/$', views.PostEaterDeleteView.as_view(), name="posteater_delete"),
    url(r'^koken/$',views.PostCookCreateView.as_view(), name="postcook_create"),
    url(r'^koken/list/$', views.PostCookListView.as_view(), name="postcook_list"),
    url(r'^koken/(?P<pk>\d+)$', views.PostCookDetailView.as_view(), name="postcook_detail"),
    url(r'^koken/(?P<pk>\d+)/aanpassen/$', views.PostCookUpdateView.as_view(), name="postcook_update"),
    url(r'^koken/(?P<pk>\d+)/verwijder/$', views.PostCookDeleteView.as_view(), name="postcook_delete"),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[-\w]+)/(?P<day>[0-9]+)/$', views.PostDayArchiveView.as_view(), name="archive_day")
]
