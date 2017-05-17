from django.test import TestCase
from modules.usuario.models import *
from modules.core.validators import *
#from django.utils import timezone
#from django.core.urlresolvers import reverse
#from whatever.forms import WhateverForm


class ValidatorsTest(TestCase):

    def test_emtpy_validator(self):
        self.assertEqual(is_empty(""), True, "Testar Validacao de valor vazio para campo vazio (OK)")
        self.assertEqual(is_empty("teste"), False, "Testar Validacao de valor vazio para campo preenchido (OK)")

    def test_contain_minimal_size_validator(self):
        self.assertEqual(contain_minimal_size("", 8), False, "Testar Validacao de valor com tamanho minimo para campo vazio (OK)")
        self.assertEqual(contain_minimal_size("123", 8), False, "Testar Validacao de valor com tamanho minimo para campo com poucos caracteres (OK)")
        self.assertEqual(contain_minimal_size("qweasdzx", 8), True, "Testar Validacao de valor com tamanho minimo para campo com tamanho igual ao minimo (OK)")
        self.assertEqual(contain_minimal_size("asdqwezxc2312", 8), True,"Testar Validacao de valor com tamanho minimo para campo com tamanho maior que o minimo (OK)")

    def test_contain_numbers_validator(self):
        self.assertEqual(contain_numbers(""), False,"Testar se campo vazio contem numeros (OK)")
        self.assertEqual(contain_numbers("ASD"), False, "Testar se campo preenchido com letras contem numeros (OK)")
        self.assertEqual(contain_numbers("ASD23dda"), True, "Testar se campo com alphanumericos contem numeros (OK)")
        self.assertEqual(contain_numbers("12313"), True, "Testar se campo contendo somente numeros contem numeros (OK)")

    def test_contain_alpha_validator(self):
        self.assertEqual(contain_alpha(""), False, "Testar se campo vazio contem letras (OK)")
        self.assertEqual(contain_alpha("12313"), False, "Testar se campo contendo somente numeros contem letras (OK)")
        self.assertEqual(contain_alpha("ASD23dda"), True, "Testar se campo com alphanumericos contem letras (OK)")
        self.assertEqual(contain_alpha("ASD"), True, "Testar se campo preenchido com letras contem letras (OK)")




