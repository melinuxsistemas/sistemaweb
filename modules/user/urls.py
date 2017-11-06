from django.conf.urls import url
from modules.user.api import UsuarioAPI, PermissionAPI

urlpatterns = [
    url(r'register/save$', UsuarioAPI.register_user),
    url(r'login/autentication$', UsuarioAPI.login_autentication),
    url(r'change_password$', UsuarioAPI.change_password),
    url(r'reset_password$', UsuarioAPI.reset_password),
    url(r'^reactivate$', UsuarioAPI.generate_new_activation_code),

    # APIs administrativas
    url(r'register/delete/(?P<email>[^/]+)/', UsuarioAPI.register_delete),
    url(r'load/permissions/(?P<id>[^/]+)/', PermissionAPI.load)
]