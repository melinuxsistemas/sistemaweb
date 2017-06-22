from django.conf.urls import url
from modules.usuario.api import UsuarioAPI

urlpatterns = [
    url(r'register/save$', UsuarioAPI.register_save),
    url(r'login/autentication$', UsuarioAPI.login_autentication),
    url(r'change_password$', UsuarioAPI.change_password),
    url(r'register/delete/(?P<email>[^/]+)/', UsuarioAPI.register_delete),
]