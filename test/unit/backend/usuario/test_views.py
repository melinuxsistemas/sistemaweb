import json

from django.test import TestCase, Client
from modules.usuario.models import Usuario


class UsuarioViewsTests(TestCase):
    def setUp(self):
            self.client = Client()

    def test_login_with_valid_user(self):
        casos_testes = [
            ['testeteste.com.br', '1q2w3e4r', False],
            ['teste@teste.com.br', '123', False],
            ['teste@teste.com.br', '1q2w3e4r', True]
        ]

        usuario = Usuario.objects.criar_usuario_contratante('teste@teste.com.br', '1q2w3e4r')
        for email,senha,resultado in casos_testes:
            response = self.client.post('/api/usuario/login/autentication',data={'email': email, 'senha': senha},HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            response_content = json.loads(response.content.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response_content['success'], resultado)
            self.client.get('/logout')

    def test_register_with_valid_user(self):
        casos_testes = [
            ['testeteste.com.br', '1q2w3e4r', '1q2w3', False],
            ['teste@teste.com.br', '1234', '123', False],
            ['teste@teste.com.br', '1q2w3e4r', '1q2w3e4r', True]
        ]

        for email, senha, confirma_senha, retorno in casos_testes:
            response = self.client.post('/api/usuario/register/save',
                                        data={'email': email, 'senha': senha, 'confirma_senha' : confirma_senha },
                                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            response_content = json.loads(response.content.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response_content['success'], retorno)
            self.client.get('/logout')