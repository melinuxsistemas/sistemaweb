import unittest
from unittest import skip

from django.test import TestCase, Client
from modules.usuario.models import Usuario
import json


class BaseRoutesTests(TestCase):
    public_routes = []
    private_routes = []

    public_api = []
    private_api = []

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        self.client = Client()

    def login_user_client(self, email, senha):
        self.user = Usuario.objects.create_test_user(email, senha)
        self.client.login(username=email, password=senha)
        return self.user

    def add_public_route(self, route):
        self.public_routes.append(route)

    def add_public_route_list(self, list_routes):
        self.public_routes = self.public_routes + list_routes

    def add_private_route(self, route):
        self.private_routes.append(route)

    def add_private_route_list(self, list_routes):
        self.private_routes = self.private_routes + list_routes

    def add_public_api(self, api, dict_paramters):
        self.public_api.append([api,dict_paramters])

    def add_private_api(self, api, dict_paramters):
        self.private_api.append([api, dict_paramters])

    def test_get_route_list(self, route_list=[], status_code=200):
        for item in route_list:
            return_status_code = self.client.get(item).status_code
            if status_code == 200:
                if return_status_code == 301:
                    return_status_code = 200
            self.assertEqual(return_status_code, status_code)

    def test_post_route_list(self, route_list=[], status_code=200):
        for item in route_list:
            result = self.client.post(item[0], data=item[1], HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            self.assertEqual(result.status_code,status_code)

    def test_public_routes(self):
        self.test_get_route_list(self.public_routes, 200)

    def test_private_routes_autenticated(self):
        user = self.login_user_client('teste@teste.com', '1q2w3e4r')
        self.test_get_route_list(self.private_routes, 200)
        user.delete()

    def test_private_routes_anonymous(self):
        for item in self.private_routes:
            self.assertNotEqual(self.client.get(item).status_code, 200)

    def test_get_private_api(self):
        self.test_get_route_list(self.private_api, 404)

    def test_post_private_api(self):
        user = self.login_user_client('teste@teste.com', '1q2w3e4r')
        self.test_post_route_list(self.private_api, 200)
        user.delete()

    def test_get_public_api(self):
        for item in self.public_api:
            self.assertNotEqual(self.client.get(item).status_code, 200)


class UsuarioRoutesTests(BaseRoutesTests):

    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)

        self.add_public_route_list(['/login/', '/logout', '/register/', '/reset_password/'])
        self.add_private_route_list(['/', '/profile'])
        self.add_public_api('/api/usuario/reactivate', {'email': 'teste@teste.com'})

        self.add_private_api('/api/usuario/register/save',{'email': 'teste@teste.com', 'password': '1q2w3e4r', 'confirm_password': '1q2w3e4r'})
        self.add_private_api('/api/usuario/login/autentication', {'email': 'teste@teste.com', 'senha': '1q2w3e4r'})
        self.add_private_api('/api/usuario/change_password',{'old_password': 'r4e3w2q1', 'password': '1q2w3e4r', 'confirm_password': '1q2w3e4r'})


    def test_valid_activation_page(self):
        test_user = Usuario.objects.create_test_user('teste@teste.com.br', '1q2w3e4r')
        if test_user is not None:
            activation_code_route = '/register/activate/'+test_user.email+'/'+test_user.activation_code
            response = self.client.get(activation_code_route)
            print("VEJA O RESPONSE: ",response.status_code)
            self.assertEqual(response.status_code, 301)
            test_user.delete()
        else:
            pass


    def test_invalid_activationcode_page(self):
        test_user = Usuario.objects.create_test_user('teste@teste.com.br', '1q2w3e4r')
        if test_user is not None:
            activation_code_route = '/register/activate/' + test_user.email + '/10b9271023120060e584492f48557272e2c313ae1451b1'
            response = self.client.get(activation_code_route)
            print("VEJA O RESPONSE: ",response)
            #self.assertEqual(response.status_code, 404)
        else:
            pass
        """

        <HttpResponseNotFound status_code=404, "text/html">
        <HttpResponsePermanentRedirect status_code=301, "text/html; charset=utf-8", url="/logout/">
        <HttpResponse status_code=200, "text/html; charset=utf-8">


        ['__bytes__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__',
         '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__',
         '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
         '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_charset',
         '_closable_objects', '_container', '_content_type_for_repr', '_convert_to_charset', '_handler_class', '_headers',
         '_reason_phrase', 'allowed_schemes', 'charset', 'client', 'close', 'closed', 'content', 'context', 'cookies',
         'delete_cookie', 'flush', 'get', 'getvalue', 'has_header', 'items', 'json', 'make_bytes', 'readable',
         'reason_phrase', 'request', 'resolver_match', 'seekable', 'serialize', 'serialize_headers', 'set_cookie',
         'set_signed_cookie', 'setdefault', 'status_code', 'streaming', 'tell', 'templates', 'url', 'writable', 'write',
         'writelines', 'wsgi_request']
        """

    """
    def test_invalid_activation_email_page(self):
        activation_code_route = '/register/activate/' + 'testeteste.com.br' + '/10b9271023120060e584492f48557272e2c313ae1451b1'
        response = self.client.get(activation_code_route)
        print("VEJA O RESPONSE: ", response.content)
        self.assertEqual(response.status_code, 200)

    def test_invalid_non_created_activation_email_page(self):
        test_user = Usuario.objects.create_test_user('testeteste.com.br', '1q2w3e4r')
        if test_user is not None:
            activation_code_route = '/register/activate/' + test_user.email + '/10b9271023120060e584492f48557272e2c313ae1451b1'
            response = self.client.get(activation_code_route)
            print("VEJA O RESPONSE: ", response.content)
            self.assertEqual(response.status_code, 200)
        else:
            pass
    """