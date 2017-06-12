import unittest
from django.test import TestCase
from modules.core.forms import FormAbstractPassword
from modules.core.forms import FormAbstractConfirmPassword
from modules.core.forms import FormAbstractEmail
from modules.usuario.forms import FormChangePassword
from rebar.testing import flatten_to_dict

from test.unit.backend.core.test_forms import TestAbstractForm


class ChangePasswordFormTest(TestAbstractForm):

    def __init__(self, *args, **kwargs):
        super(ChangePasswordFormTest, self).__init__()
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.set_formulary(FormChangePassword)

        self.add_case_invalid_format({'old_password': None,'password': None,'confirm_password': None}, "Test not acepted null values for all fields (OK)")
        self.add_case_invalid_format({'old_password': '1q2w3e4r', 'password': '1234qwer', 'confirm_password': '1234qwerp'},"Test not acepted password and confirm password diferents (OK)")
        """
        self.add_case_invalid_format({'email': ""}, "Test empty email values (OK)")
        self.add_case_invalid_format({'email': '@teste.com'}, "Test email without user email (OK)")
        self.add_case_invalid_format({'email': 'teste2@.com'}, "Test email without domain (OK)")
        self.add_case_invalid_format({'email': 'teste2@teste@.com'}, "Test email with two '@' character (OK)")
        self.add_case_invalid_format({'email': 'teste2.com'}, "Test email without '@' character (OK)")
        self.add_case_invalid_format({'email': 'teste+001@gmail.com'}, "Test email with dangerous symbols (OK)")

        self.add_case_valid_format({'email': 'teste@teste.com'}, "Test valid format email values (OK)")
        self.add_case_valid_format({'email': 'teste_testes@teste.com'},
                                   "Test valid format email with '_' character (OK)")
        self.add_case_valid_format({'email': 'teste5@teste.com'}, "Test valid format email with number (OK)")
        self.add_case_valid_format({'email': '10teste@teste.com'},
                                   "Test valid format email initialized by with number (OK)")

        big_value_email = '1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t@1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t.com.br'
        self.add_case_valid_size({'email': 'teste@teste.com'}, "Test email with normal size values (OK)")
        self.add_case_invalid_size({'email': big_value_email}, "Test email with exceded size values (OK)")
        """


"""
class EmailFormTests (TestCase):

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
            form_data = flatten_to_dict(())
            form_data["email"] = item[0]
            form = FormAbstractEmail(data=form_data)
            #print('formulario form_data', form_data)
            #print('variavel form:', form)
            resultado = form.is_valid()
            #print(resultado)
            #if resultado != item[1] :
            #    print ("erros:",form.errors )
            #print(item[0],item[1], resultado)
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
"""



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





