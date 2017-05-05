from django.conf.urls import url
from modules.usuario import views

urlpatterns = [
    #url(r'', views.index),
    url(r'^$', views.index),
    url(r'^usuario/register/$', views.register),
    url(r'^usuario/login/$', views.login),
    url(r'^usuario/grava_novo/$', views.grava_novo),

]