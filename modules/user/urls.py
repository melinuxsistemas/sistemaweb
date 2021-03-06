from django.conf.urls import url
from modules.user.api import UserController, PermissionAPI

urlpatterns = [
    url(r'register/save$', UserController().register_user),
    url(r'login/autentication$', UserController().login_autentication),
    url(r'reset_password$', UserController().reset_password),
    url(r'change_password$', UserController().change_password),
    url(r'reactivate$', UserController().resend_activation_code),

    # User Administration
    url(r'filter/', UserController.filter_users),
    # APIs administrativas
    url(r'register/delete/(?P<email>[^/]+)/', UserController.register_delete),
    url(r'load/permissions/(?P<id>[^/]+)/', PermissionAPI.load),
    url(r'save/permissions/', PermissionAPI.save)
]
