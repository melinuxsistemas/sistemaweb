from django.core.exceptions import PermissionDenied, ValidationError
from sistemaweb import settings
from functools import wraps


def request_ajax_required(view):
    @wraps(view)
    def _wrapped_view(controller, request, formulary, *args, **kwargs):
        """ request via ajax verifiy need settings.DEBUG=True for running view tests."""
        if request.is_ajax() or settings.DEBUG:
            return view(controller, request, formulary, *args, **kwargs)
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
            return view(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    return _wrapped_view