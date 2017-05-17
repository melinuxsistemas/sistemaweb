import json

from django.contrib.auth import login

from django.test import TestCase, Client
from django.utils.http import urlencode

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