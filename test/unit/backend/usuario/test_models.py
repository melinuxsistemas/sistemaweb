from django.test import TestCase
from modules.usuario.models import Usuario
#from django.utils import timezone
#from django.core.urlresolvers import reverse
#from whatever.forms import WhateverForm


class UsuarioTest(TestCase):

    def test_criar_contratante(self):
        usuario = Usuario.objects.criar_usuario_contratante('teste@teste.com','1q2w3e4r')
        self.assertTrue(isinstance(usuario, Usuario), 'Objeto criado instanciado corretamente (OK)')
        self.assertEqual(usuario.__unicode__(), usuario.email,"Representacao do objeto com unicode (OK)")
