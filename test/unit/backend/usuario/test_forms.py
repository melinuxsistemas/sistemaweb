import unittest

from rebar.testing import flatten_to_dict
from django.test import TestCase
from modules.core.forms import FormAbstractPassword
from modules.core.forms import FormAbstractConfirmPassword
from modules.core.forms import FormAbstractEmail
from modules.usuario.forms import FormChangePassword

"""
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
        
"""


class PasswordFormTests(TestCase):

    def test_form_password_valid_size(self):
        form_data = flatten_to_dict(FormAbstractPassword())
        form_data['password'] = '7caract'
        form = FormAbstractPassword(data=form_data)
        self.assertFalse(form.is_valid(), 'Testar se a senha possui tamanho minimo de 8 caracteres')

        form_data['password'] = '0123456789012345678901234567890123456789012345678ab'
        form = FormAbstractPassword(data=form_data)
        self.assertEquals(form.is_valid(), False, 'Testas se a senha contem mais de 50 caracteres (OK)')

    def test_form_password_valid_format(self):
        form_data = flatten_to_dict(FormAbstractPassword())
        form_data['password'] = '1234a$bc'
        form = FormAbstractPassword(data=form_data)
        self.assertEquals(form.is_valid(), False, 'Testar se a senha contem caracters especiais (OK)')

        form_data['password'] = '1234abcd'
        form = FormAbstractPassword(data=form_data)
        self.assertEquals(form.is_valid(),True, 'Testar se a senha atende todos os requisitos (OK)')

        form_data['password'] = ''
        form = FormAbstractPassword(data=form_data)
        self.assertEquals(form.is_valid(), False, 'Testar se a senha é string vazia (OK)')

        form_data['password'] = '789654123'
        form = FormAbstractPassword(data=form_data)
        self.assertEquals(form.is_valid(),False, 'Testar se a senha contem letras alem de numeros (OK)')

        form_data['password'] = 'abcdefgh'
        form = FormAbstractPassword(data=form_data)
        self.assertEquals(form.is_valid(),False, 'Testar se a senha contem numeros alem de letras (OK)')


class ConfirmPasswordFormTests(TestCase):

    def test_form_password_confirm_valid_size(self):
        form_data = flatten_to_dict(FormAbstractConfirmPassword())
        form_data['confirm_password'] = '7caract'
        form = FormAbstractConfirmPassword(data=form_data)
        self.assertFalse(form.is_valid(), 'Testar se a senha possui tamanho minimo de 8 caracteres')

        form_data['confirm_password'] = '0123456789012345678901234567890123456789012345678ab'
        form = FormAbstractConfirmPassword(data=form_data)
        self.assertEquals(form.is_valid(), False, 'Testas se a senha contem mais de 50 caracteres (OK)')

    def test_form_password_confirm_valid_format(self):
        form_data = flatten_to_dict(FormAbstractConfirmPassword())
        form_data['confirm_password'] = '1234a$bc'
        form = FormAbstractConfirmPassword(data=form_data)
        self.assertEquals(form.is_valid(), False, 'Testar se a senha contem caracters especiais (OK)')

        form_data['confirm_password'] = '1234abcd'
        form = FormAbstractConfirmPassword(data=form_data)
        self.assertEquals(form.is_valid(),True, 'Testar se a senha atende todos os requisitos (OK)')

        form_data['confirm_password'] = ''
        form = FormAbstractConfirmPassword(data=form_data)
        self.assertEquals(form.is_valid(), False, 'Testar se a senha é string vazia (OK)')

        form_data['confirm_password'] = '789654123'
        form = FormAbstractConfirmPassword(data=form_data)
        self.assertEquals(form.is_valid(),False, 'Testar se a senha contem letras alem de numeros (OK)')

        form_data['confirm_password'] = 'abcdefgh'
        form = FormAbstractConfirmPassword(data=form_data)
        self.assertEquals(form.is_valid(),False, 'Testar se a senha contem numeros alem de letras (OK)')


class EmailFromTests (TestCase):

    def test_form_email_valid (self):
        variacoes = [
            [None, False],
            ['', False],
            ['@teste.com', False],
            ['teste2@.com', False],
            ['teste2@teste@.com', False],
            ['teste2.com', False],
            ['teste+001@gmail.com', False],
            ['teste@teste.com', True],
            ['teste2@gmail.com', True],
            ['teste_teste@teste.com', True]
        ]

        for item in variacoes:
            form_data = flatten_to_dict(FormAbstractEmail())
            form_data["email"] = item[0]
            form = FormAbstractEmail(data=form_data)
            print('formulario form_data', form_data)
            print('variavel form:', form)
            resultado = form.is_valid()
            print(resultado)
            if resultado != item[1] :
                print ("erros:",form.errors )
            print(item[0],item[1], resultado)
            self.assertEquals(resultado, item[1],'Usuario Contratante instanciado corretamente (OK)')

class ChangePasswordFormTest(TestCase):

    def test_form_old_password_valid(self):

        
        set_fields = '1q2w3e4r'
        variacoes_old_password = [
            [None, False],
            ['', False],
            ['f4ltaum', False],
            ['0123456789012345678901234567890123456789012345678ab', False],
            ['1234a$bc', False],
            ['789654123', False],
            ['abcdefgh',False],
            ['1234abcd',True]
            
        ]   
        
        for item in variacoes_old_password:
            form_data = flatten_to_dict(FormChangePassword())
            form_data['old_password'] = set_fields
            form_data['password'] = set_fields
            form_data['confirm_password'] = item[0]
            form = FormChangePassword(data=form_data)
            self.assertEquals(form.is_valid(),item[1], 'Testar se old passwor é valido (OK)')
    
''' def test_combined_fields(self):
        variacoes_de_teste = [
            ['abcd1234','1234abcd','1234abcd', True ,'Testar se atente todos requesitos (OK)'],
            ['abcd1234','abcd1234','abcd1234', False,'Testar se senha antiga é igual a nova (OK)'],
            ['abcd1234','1234abcd','1234dife', False,'Testar se as senhas novas são diferente'],
            ['abcd1234','invalido','1234abcd', False,'Testa se a nova senha é invalida']
        ]

        for item in variacoes_de_teste:
            form_data = flatten_to_dict(FormChangePassword())

            form_data['old_password'] = item[0]
            form_data['password'] = item[1]
            form_data['confirm_password'] = item[2]
            form = FormChangePassword(data=form_data)
            self.assertEquals(form.is_valid(),item[3], item[4])'''





