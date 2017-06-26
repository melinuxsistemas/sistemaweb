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

        usuario = Usuario.objects.create_contracting_user('teste@teste.com.br', '1q2w3e4r')
        """
        for email,senha,resultado in casos_testes:
            response = self.client.post('/api/usuario/login/autentication',data={'email': email, 'senha': senha},HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            response_content = json.loads(response.content.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response_content['success'], resultado)
            self.client.get('/logout')
        """

    def test_register_with_valid_user(self):
        casos_testes = [
            ['teste@teste.com.br', '1q2w3e4r', '1q2w3e4r', True],
            ['testeteste.com.br', '1q2w3e4r', '1q2w3', False],
            ['teste@teste.com.br', '1234', '123', False]

        ]

        for email, senha, confirma_senha, retorno in casos_testes:
            response = self.client.post('/api/usuario/register/save',data={'email': email, 'password': senha, 'confirm_password' : confirma_senha },HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            response_content = json.loads(response.content.decode())
            print("Status code: ",response_content)
            self.assertEqual(response.status_code, 200)
            #print('Teste Respons:   ',response_content['success'], retorno)
            self.assertEqual(response_content['success'], retorno)
            self.client.get('/logout')