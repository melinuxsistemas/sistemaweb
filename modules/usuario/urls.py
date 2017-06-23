from django.conf.urls import url
from modules.usuario.api import UsuarioAPI

urlpatterns = [
    url(r'register/save$', UsuarioAPI.register_user),
    url(r'login/autentication$', UsuarioAPI.login_autentication),
    url(r'change_password$', UsuarioAPI.change_password),
    url(r'reset_password$', UsuarioAPI.reset_password),
    url(r'^reactivate$', UsuarioAPI.generate_activation_code),
]