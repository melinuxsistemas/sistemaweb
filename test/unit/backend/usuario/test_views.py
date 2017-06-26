from django.test import TestCase, Client
from modules.usuario.models import Usuario
import json


class UsuarioViewsTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_with_valid_user(self):
        casos_testes = [
            ['testeteste.com.br', '1q2w3e4r', False],
            ['teste@teste.com.br', '123', False],
            ['teste@teste.com.br', '1q2w3e4r', True]
        ]

        for email, password, resultado in casos_testes:
            user = Usuario.objects.create_test_user(email, password)
            response = self.client.post('/api/usuario/login/autentication', data={'email': email, 'password': password},HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            response_content = json.loads(response.content.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response_content['success'], resultado)
            self.client.get('/logout')
            if user is not None:
                user.delete()
            else:
                self.assertEqual(response_content['data-object'], None)

    def test_register_with_valid_user(self):
        casos_testes = [
            ['teste@teste.com.br', '1234', '123', False],
            ['testeteste.com.br', '1q2w3e4r', '1q2w3', False],
            ['teste@teste.com.br', '1q2w3e4r', '1q2w3e4r', True]
        ]

        for email, password, confirm_password, retorno in casos_testes:
            response = self.client.post('/api/usuario/register/save',data={'email': email, 'password': password, 'confirm_password' : confirm_password },HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            response_content = json.loads(response.content.decode())
            print("RESPONSE CONTENT: ",response_content)
            #self.assertEqual(response.status_code, 200)
            #print('Teste Respons:   ',response_content['success'], retorno)
            #self.assertEqual(response_content['success'], retorno)
            #self.client.get('/logout')