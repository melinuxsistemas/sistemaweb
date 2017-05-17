from django.test import TestCase
from modules.usuario.models import *
#modules.usuario.models import Usuario
#from django.utils import timezone
#from django.core.urlresolvers import reverse
#from whatever.forms import WhateverForm


class UsuarioTest(TestCase):

    def test_criar_contratante(self):
        usuario = Usuario.objects.criar_usuario_contratante('teste@teste.com','1q2w3e4r')
        self.assertTrue(isinstance(usuario, Usuario), 'Usuario Contratante instanciado corretamente (OK)')
        self.assertEqual(usuario.__unicode__(), usuario.email,"Representacao do objeto com unicode (OK)")

    def test_verificar_email_valido(self):
        variacoes = [
            ['teste@teste.com', True],
            ['teste2@teste.com', True],
            ['@teste.com', False],
            ['teste2@teste.com', True],
            ['teste2@teste@.com', False],
            ['teste2.com', False],
        ]

        #for item in variacoes:
        #    usuario = Usuario.objects.criar_usuario_contratante(item[0], '1q2w3e4r')
        #    #self.assertEqual(len(usuario.password), 77, "Criacao de senhas criptografa com tamanho regular (OK)")


    def test_verificar_criptografia(self):
        variacoes = [('teste@teste.com','1q2w3e4r'),('teste2@teste.com','123qweasd23')]
        for item in variacoes:
            usuario = Usuario.objects.criar_usuario_contratante(item[0],item[1])
            self.assertEqual(len(usuario.password), 77, "Criacao de senhas criptografa com tamanho regular (OK)")




