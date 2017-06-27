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
        self.test_get_route_list(self.public_api, 200)
        # self.assertEqual(self.test_route_list(self.client.get, self.private_api, 404), True)


class UsuarioRoutesTests(BaseRoutesTests):

    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)
        self.add_public_route_list(['/login/', '/logout', '/register/','/reset_password/'])
        self.add_private_route_list(['/', '/profile'])

        self.add_private_api('/api/usuario/register/save',{'email': 'teste@teste.com', 'password': '1q2w3e4r', 'confirm_password': '1q2w3e4r'})
        """


        self.add_private_api('/api/usuario/new_register',  {'email': 'teste@teste.com'})
        self.add_private_api('/api/usuario/login/autentication',{'email': 'teste@teste.com', 'senha': '1q2w3e4r'})
        self.add_private_api('/api/usuario/change_password',{'old_password':'r4e3w2q1' , 'password': '1q2w3e4r', 'confirm_password': '1q2w3e4r'})
        self.add_private_api('/api/usuario/activate',{'email': 'teste@teste.com','chave' : 'ce11f7102ce87660c93ed415d2a7102da6625049645173'})
        self.add_private_api('/api/usuario/reset_password',{'email': 'teste@teste.com'})
        """