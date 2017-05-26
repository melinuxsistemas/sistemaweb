from django.conf import settings
from django.conf.urls import url
from modules.usuario import views
from modules.usuario.api import UsuarioAPI

urlpatterns = [
    url(r'register/save$', UsuarioAPI.register_save),
    url(r'login/autentication$', UsuarioAPI.login_autentication),
]