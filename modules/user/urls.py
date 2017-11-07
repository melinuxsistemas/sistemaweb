from django.conf.urls import url
from modules.user.api import UserController, PermissionAPI

urlpatterns = [
    url(r'register/save$', UserController().register_user),
    url(r'login/autentication$', UserController().login_autentication),
    url(r'change_password$', UserController.change_password),
    url(r'reset_password$', UserController.reset_password),
    url(r'^reactivate$', UserController.generate_new_activation_code),

    # APIs administrativas
    url(r'register/delete/(?P<email>[^/]+)/', UserController.register_delete),
    url(r'load/permissions/(?P<id>[^/]+)/', PermissionAPI.load)
]