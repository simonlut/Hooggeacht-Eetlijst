from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    url(r"login/$", auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name="logout"),
    url(r'signup/$', views.SignUp.as_view(), name="signup"),
    url(r'profile/$', views.update_profile, name="profile"),
    url(r'^aanhang/$',views.AttachmentCreateView.as_view(), name="attachment_create"),
    url(r'^aanhang/list/$', views.AttachmentListView.as_view(), name="attachment_list"),
    url(r'^aanhang/(?P<pk>\d+)$', views.AttachmentDetailView.as_view(), name="attachment_detail"),
    url(r'^aanhang/(?P<pk>\d+)/aanpassen/$', views.AttachmentUpdateView.as_view(), name="attachment_update"),
    url(r'^aanhang/(?P<pk>\d+)/verwijder/$', views.AttachmentDeleteView.as_view(), name="attachment_delete"),
]

    # url(r'account_settings/$', views.AccountSettings.as_view(), name="accountsettings"),
