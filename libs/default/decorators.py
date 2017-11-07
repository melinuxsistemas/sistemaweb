from django.core.exceptions import PermissionDenied
from sistemaweb import settings
from functools import wraps


def request_ajax_required(view):
    @wraps(view)
    def _wrapped_view(request, *args, **kwargs):
        """ request via ajax verifiy need settings.DEBUG=True for running view tests."""
        if request.is_ajax() or settings.DEBUG:
            return view(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    return _wrapped_view


def request_get_required(view):
    @wraps(view)
    def _wrapped_view(request, *args, **kwargs):
        if request.method == 'GET':
            return view(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    return _wrapped_view


def request_post_required(view):
    @wraps(view)
    def _wrapped_view(request, *args, **kwargs):
        if request.method == 'POST':
            print("EH POST")
            return view(request, *args, **kwargs)
        else:
            print("NAO EH POST")
            raise PermissionDenied()
    return _wrapped_view