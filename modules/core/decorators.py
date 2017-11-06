from functools import wraps

from django.core.exceptions import PermissionDenied
from django.utils.decorators import available_attrs

from sistemaweb import settings


#def required_condition(request,function):
#    def _decorator(request, *args, **kwargs):
#        if function():
#            return True
#        else:
#            return False
#    return wraps(function)(_decorator)


#@method_decorator(user_passes_test(lambda u: u.is_authenticated() and u.is_superuser))

def required_permission(function):
    @wraps(function, assigned=available_attrs(function))
    def _wrapped_view(request, *args, **kwargs):
        print("CONSIGO USAR A FUNCAO DA CLASSE COM PASSANDO O REQUEST USER? ",request," ARGUMENTO", request.user)
        print("DECORATOR - VERIFIY PERMISSION: ",function, request)

        if function(request.user):
            return request
        else:
            raise PermissionDenied
    _wrapped_view.__doc__ = function.__doc__
    _wrapped_view.__name__ = function.__name__
    return _wrapped_view




def request_is_valid(function):
    def wrap(request, *args, **kwargs):
        if request.is_ajax() or settings.DEBUG:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
