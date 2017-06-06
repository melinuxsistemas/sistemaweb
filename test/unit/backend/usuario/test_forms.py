import unittest

from rebar.testing import flatten_to_dict
from django.test import TestCase
from modules.usuario.forms import form_abstract_password
from modules.usuario.forms import form_abstract_confirm_password


class AbstractPasswordFormTests(TestCase):

    lst_fields = []

    def set_form (self,form):
        self.form = form

    def __init__(self,form, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        self.form = self.form()
        self.form_data = flatten_to_dict(self.form)


    def test_form_password_valid_size(self):
        for field,value in self.lst_fields:
            self.form_data[field] = value
            self.assertFalse(self.form.is_valid(), 'Testar se a senha possui tamanho minimo de 8 caracteres')


class TestPassword (AbstractPasswordFormTests):
    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)
        self.set_form(form_abstract_password)
        self.lst_fields = [['password','1234567890']]


class PasswordFormTests(TestCase):

    def test_form_password_valid_size(self):
        form_data = flatten_to_dict(form_abstract_password())
        form_data['password'] = '7caract'
        form = form_abstract_password(data=form_data)
        self.assertFalse(form.is_valid(), 'Testar se a senha possui tamanho minimo de 8 caracteres')

        form_data['password'] = '0123456789012345678901234567890123456789012345678ab'
        form = form_abstract_password(data=form_data)
        self.assertEquals(form.is_valid(), False, 'Testas se a senha contem mais de 50 caracteres (OK)')

    def test_form_password_valid_format(self):
        form_data = flatten_to_dict(form_abstract_password())
        form_data['password'] = '1234a$bc'
        form = form_abstract_password(data=form_data)
        self.assertEquals(form.is_valid(), False, 'Testar se a senha contem caracters especiais (OK)')

        form_data['password'] = '1234abcd'
        form = form_abstract_password(data=form_data)
        self.assertEquals(form.is_valid(),True, 'Testar se a senha atende todos os requisitos (OK)')

        form_data['password'] = ''
        form = form_abstract_password(data=form_data)
        self.assertEquals(form.is_valid(), False, 'Testar se a senha é string vazia (OK)')

        form_data['password'] = '789654123'
        form = form_abstract_password(data=form_data)
        self.assertEquals(form.is_valid(),False, 'Testar se a senha contem letras alem de numeros (OK)')

        form_data['password'] = 'abcdefgh'
        form = form_abstract_password(data=form_data)
        self.assertEquals(form.is_valid(),False, 'Testar se a senha contem numeros alem de letras (OK)')


class ConfirmPasswordFormTests(TestCase):

    def test_form_password_confirm_valid_size(self):
        form_data = flatten_to_dict(form_abstract_confirm_password())
        form_data['confirm_password'] = '7caract'
        form = form_abstract_confirm_password(data=form_data)
        self.assertFalse(form.is_valid(), 'Testar se a senha possui tamanho minimo de 8 caracteres')

        form_data['confirm_password'] = '0123456789012345678901234567890123456789012345678ab'
        form = form_abstract_confirm_password(data=form_data)
        self.assertEquals(form.is_valid(), False, 'Testas se a senha contem mais de 50 caracteres (OK)')

    def test_form_password_confirm_valid_format(self):
        form_data = flatten_to_dict(form_abstract_confirm_password())
        form_data['confirm_password'] = '1234a$bc'
        form = form_abstract_confirm_password(data=form_data)
        self.assertEquals(form.is_valid(), False, 'Testar se a senha contem caracters especiais (OK)')

        form_data['confirm_password'] = '1234abcd'
        form = form_abstract_confirm_password(data=form_data)
        self.assertEquals(form.is_valid(),True, 'Testar se a senha atende todos os requisitos (OK)')

        form_data['confirm_password'] = ''
        form = form_abstract_confirm_password(data=form_data)
        self.assertEquals(form.is_valid(), False, 'Testar se a senha é string vazia (OK)')

        form_data['confirm_password'] = '789654123'
        form = form_abstract_confirm_password(data=form_data)
        self.assertEquals(form.is_valid(),False, 'Testar se a senha contem letras alem de numeros (OK)')

        form_data['confirm_password'] = 'abcdefgh'
        form = form_abstract_confirm_password(data=form_data)
        self.assertEquals(form.is_valid(),False, 'Testar se a senha contem numeros alem de letras (OK)')





