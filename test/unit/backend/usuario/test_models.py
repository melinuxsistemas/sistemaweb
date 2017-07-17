from django.test import TestCase
from modules.user.models import *

class UsuarioTest(TestCase):

    def test_create_user(self):
        usuario = User.objects.create_contracting_user('teste@teste.com', '1q2w3e4r')
        self.assertTrue(isinstance(usuario, User), 'Usuario Contratante instanciado corretamente (OK)')
        self.assertEqual(usuario.__unicode__(), usuario.email,"Representacao do objeto com unicode (OK)")

    def test_validation_create_user(self):
        variacoes = [
            [None, False],
            ['', False],
            ['@teste.com', False],
            ['teste2@.com', False],
            ['teste2@teste@.com', False],
            ['teste2.com', False],
            ['teste+001@gmail.com', False],
            ['teste@teste.com', True],
            ['teste2@teste.com', True],
            ['teste_teste@teste.com', True]
        ]

        for item in variacoes:
            usuario = User.objects.create_contracting_user(item[0], '1q2w3e4r')
            self.assertEqual((isinstance(usuario, User)),item[1], 'Usuario Contratante instanciado corretamente (OK)')

    def test_authenticate_user(self):
        usuario = User.objects.create_contracting_user('teste@teste.com', '1q2w3e4r')
        usuario_autenticado = User.objects.authenticate(None, email='teste@teste.com', password='1234567')
        self.assertNotEqual(usuario.__unicode__(), usuario_autenticado,"Teste autenticação de usuário com senha incorreta (OK)")

        usuario_autenticado = User.objects.authenticate(None, email='teste@teste.com', password='1q2w3e4r')
        self.assertEqual(usuario.__unicode__(), usuario_autenticado.__unicode__(),"Teste de autenticação com usuário e senha corretos (OK)")

    def test_verify_criptography(self):
        variacoes = [('teste@teste.com','1q2w3e4r'),('teste2@teste.com','123qweasd23')]
        for item in variacoes:
            usuario = User.objects.create_contracting_user(item[0], item[1])
            self.assertEqual(len(usuario.password), 77, "Criacao de senhas criptografa com tamanho regular (OK)")

