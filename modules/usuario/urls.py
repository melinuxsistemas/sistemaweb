from django.conf.urls import url
from modules.usuario import views

urlpatterns = [
    #url(r'', views.index),
    url(r'register/save$', views.register_save),


]