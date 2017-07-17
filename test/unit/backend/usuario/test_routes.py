import unittest
from unittest import skip

from django.test import TestCase, Client
from modules.user.models import User
import json


class StatusCode:
    """ Status de sucesso na requisicao """
    request_success = 200
    #201 Criado (Created)
    #202 Aceito (Accepted)
    #203 Informação não autorativa (Non-Authorative Information)
    #204 Sem conteúdo (No Content)
    #205 Conteúdo apagado (Reset Content)
    #206 Conteúdo parcial (Partial Content)

    """ Status de redirecionamentos na requisicao """
    #300 Escolhas múltiplas (Multiple Choices)
    request_redirected_permanently = 301 # Mudado permanentemente (Moved Permanently), provavelmente por conta de uma '/' no final da rota.
    request_redirected             = 302 # Mudado temporariamente (Moved Temporarily)
    #303 Veja outras (See Other)
    #304 Não modificado (Not Modified)
    #305 Use Proxy (Use Proxy)

    """ Status de erro na requisições """
    request_bad = 400 # Requisição viciada (Bad Request)
    request_authorization_required = 401 # Autorização Requerida (Authorization Required)
    request_payment_required       = 402 # Pagamento Requerido (Payment Required)
    request_forbidden              = 403 # Proibido (Forbidden)
    request_not_found              = 404  # Não encontrado (Not Found)
    #405 Método não permitido (Method Not Allowed)
    #406 Codificação não aceita (Not Acceptable (encoding)
    #407 Autenticação proxy Requerida (Proxy Authentication Required )
    #408 Requisição vencida (Request Timed Out)
    #409 Requisição conflitante (Conflicting Request)
    #410 Acabou (Gone)
    #411 Requer comprimento do conteúdo (Content Length Required)
    #412 Falha na precondição (Precondition Failed)
    #413 Entidade requerida muito longa (Request Entity Too Long)
    #414 URI requerida muito longa (Request URI Too Long)
    #415 Tipo de mídia não suportado (Unsupported Media Type)

    """ Status de erro no Servidor """
    request_internal_error = 500 # Erro interno do servidor (Internal Server Error)
    #501 Não implementado (Not Implemented)
    #502 Gateway viciado (Bad Gateway)
    #503 Serviço não disponível (Service Unavailable)
    #504 Gateway vencido (Gateway Timeout)
    #505 Versão HTTP não suportada (HTTP Version Not Supported)


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
        self.user = User.objects.create_test_user(email, senha)
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

    def test_get_route_list(self, route_list=[], status_code=StatusCode.request_success):
        for item in route_list:
            return_status_code = self.client.get(item).status_code
            if status_code == StatusCode.request_success:
                if return_status_code == StatusCode.request_redirected_permanently:
                    return_status_code = StatusCode.request_success
            self.assertEqual(return_status_code, status_code)

    def test_post_route_list(self, route_list=[], status_code=StatusCode.request_success):
        for item in route_list:
            result = self.client.post(item[0], data=item[1], HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            self.assertEqual(result.status_code,status_code)

    def test_public_routes(self):
        self.test_get_route_list(self.public_routes, StatusCode.request_success)

    def test_private_routes_autenticated(self):
        user = self.login_user_client('teste@teste.com', '1q2w3e4r')
        self.test_get_route_list(self.private_routes, StatusCode.request_success)
        user.delete()

    def test_private_routes_anonymous(self):
        for item in self.private_routes:
            self.assertNotEqual(self.client.get(item).status_code, StatusCode.request_success)

    def test_get_private_api(self):
        self.test_get_route_list(self.private_api, StatusCode.request_not_found)

    def test_post_private_api(self):
        user = self.login_user_client('teste@teste.com', '1q2w3e4r')
        self.test_post_route_list(self.private_api, StatusCode.request_success)
        user.delete()

    def test_get_public_api(self):
        for item in self.public_api:
            response = self.client.get(item[0],data=item[1])
            self.assertNotEqual(response.status_code, StatusCode.request_success)


class UsuarioRoutesTests(BaseRoutesTests):

    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)

        self.add_public_route_list(['/login/', '/logout', '/register/', '/reset_password/'])
        self.add_private_route_list(['/', '/profile'])
        self.add_private_api('/api/usuario/register/save',{'email': 'teste@teste.com', 'password': '1q2w3e4r', 'confirm_password': '1q2w3e4r'})
        self.add_private_api('/api/usuario/login/autentication', {'email': 'teste@teste.com', 'senha': '1q2w3e4r'})
        self.add_private_api('/api/usuario/change_password',{'old_password': 'r4e3w2q1', 'password': '1q2w3e4r', 'confirm_password': '1q2w3e4r'})

    def test_valid_activation_page(self):
        test_user = User.objects.create_test_user('outroteste@teste.com.br', '1q2w3e4r')
        activation_code = test_user.activation_code
        test_user.activation_code = None
        test_user.account_activated = False
        test_user.save()
        if test_user is not None:
            activation_code_route = '/register/activate/'+test_user.email+'/'+activation_code+"/"
            response = self.client.get(activation_code_route)
            self.assertEqual(response.status_code, StatusCode.request_redirected)
        test_user.delete()

    def test_invalid_activation_code_page(self):
        test_user = User.objects.create_test_user('teste@teste.com.br', '1q2w3e4r')
        if test_user is not None:
            activation_code_route = '/register/activate/' + test_user.email + '/10b9271023120060e584492f48557272e2c313ae1451b1/'
            response = self.client.get(activation_code_route)
            self.assertEqual(response.status_code, StatusCode.request_success)
        test_user.delete()

    def test_invalid_activation_email_page(self):
        activation_code_route = '/register/activate/' + 'testeteste.com.br' + '/10b9271023120060e584492f48557272e2c313ae1451b1/'
        response = self.client.get(activation_code_route)
        self.assertEqual(response.status_code, StatusCode.request_success)

    def test_invalid_non_registered_email_page(self):
        test_user = User.objects.create_test_user('teste@teste.com.br', '1q2w3e4r')
        if test_user is not None:
            activation_code_route = '/register/activate/teste@outroteste.com/'+test_user.activation_code+"/"
            response = self.client.get(activation_code_route)
            self.assertEqual(response.status_code, StatusCode.request_success)
        test_user.delete()

    def test_reset_password_valid_email(self):
        test_user = User.objects.create_test_user('teste@teste.com.br', '1q2w3e4r')
        response = self.client.post('/api/usuario/reset_password',data={'email':test_user.email})
        self.assertEqual(json.loads(response.content)['success'] , True)
        self.assertEqual(response.status_code, StatusCode.request_success)
        test_user.delete()

    def test_reset_password_without_email(self):
        response = self.client.post('/api/usuario/reset_password', data={})
        self.assertEqual(json.loads(response.content)['success'], False)
        self.assertEqual(response.status_code, StatusCode.request_success)

    def test_reset_password_with_empty_email(self):
        response = self.client.post('/api/usuario/reset_password', data={'email':''})
        self.assertEqual(json.loads(response.content)['success'], False)
        self.assertEqual(response.status_code, StatusCode.request_success)

    def test_reset_password_with_invalid_email(self):
        response = self.client.post('/api/usuario/reset_password', data={'email': 'teste.com.br'})
        self.assertEqual(json.loads(response.content)['success'], False)
        self.assertEqual(response.status_code, StatusCode.request_success)

    def test_reset_password_with_inexist_user(self):
        response = self.client.post('/api/usuario/reset_password', data={'email': 'teste@teste.com.br'})
        self.assertEqual(json.loads(response.content)['success'], False)
        self.assertEqual(response.status_code, StatusCode.request_success)

    def test_resend_activation_valid_email(self):
        test_user = User.objects.create_contracting_user('teste@teste.com.br', '1q2w3e4r')
        response = self.client.post('/api/usuario/reactivate', data={'email': test_user.email})
        self.assertEqual(json.loads(response.content)['success'], True)
        self.assertEqual(response.status_code, StatusCode.request_success)
        test_user.delete()

    def test_resend_activation_without_email(self):
        response = self.client.post('/api/usuario/reactivate', data={})
        self.assertEqual(json.loads(response.content)['success'], False)
        self.assertEqual(response.status_code, StatusCode.request_success)

    def test_resend_activation_empty_email(self):
        response = self.client.post('/api/usuario/reactivate', data={'email': ''})
        self.assertEqual(json.loads(response.content)['success'], False)
        self.assertEqual(response.status_code, StatusCode.request_success)

    def test_resend_activation_invalid_email(self):
        response = self.client.post('/api/usuario/reactivate', data={'email': 'testeteste.com.br'})
        self.assertEqual(json.loads(response.content)['success'], False)
        self.assertEqual(response.status_code, StatusCode.request_success)

    def test_resend_activation_inexist_email(self):
        response = self.client.post('/api/usuario/reactivate', data={'email': 'teste@teste.com.br'})
        self.assertEqual(json.loads(response.content)['success'], False)
        self.assertEqual(response.status_code, StatusCode.request_success)
