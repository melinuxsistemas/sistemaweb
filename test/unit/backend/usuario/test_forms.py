import unittest
from django.test import TestCase
from rebar.testing import flatten_to_dict
from modules.core.forms import FormAbstractPassword
from modules.core.forms import FormAbstractConfirmPassword
from modules.core.forms import FormAbstractEmail
from modules.usuario.forms import FormChangePassword
from rebar.testing import flatten_to_dict


class TestAbstractForm(TestCase):

    formulary = None
    cases_valid_format = []
    cases_invalid_format = []
    cases_valid_size = []
    cases_invalid_size = []

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.cases_valid_format = []
        self.cases_invalid_format = []
        self.cases_valid_size = []
        self.cases_invalid_size = []

    def add_case_valid_format(self, value, success_message):
        self.cases_valid_format.append(
            {'fields_value': value, 'expected_result': True, "success_message": success_message})

    def add_case_valid_format_list(self, list_case):
        self.cases_valid_format = self.cases_valid_format + list_case

    def add_case_invalid_format(self, value, success_message):
        self.cases_invalid_format.append(
            {'fields_value': value, 'expected_result': False, "success_message": success_message})

    def add_case_invalid_format_list(self, list_case):
        self.cases_invalid_format = self.cases_valid_format + list_case

    def add_case_valid_size_list(self, list_case):
        self.cases_valid_size = self.cases_valid_format + list_case

    def add_case_valid_size(self, value, success_message):
        self.cases_valid_size.append(
            {'fields_value': value, 'expected_result': True, "success_message": success_message})

    def add_case_invalid_size_list(self, list_case):
        self.cases_invalid_size = self.cases_valid_format + list_case

    def add_case_invalid_size(self, value, success_message):
        self.cases_invalid_size.append(
            {'fields_value': value, 'expected_result': False, "success_message": success_message})

    def test_form_password_valid_format(self):
        self.execute_test_list_cases(self.cases_valid_format)

    def test_form_password_invalid_format(self):
        self.execute_test_list_cases(self.cases_invalid_format)

    def test_form_password_valid_size(self):
        self.execute_test_list_cases(self.cases_valid_size)

    def test_form_password_invalid_size(self):
        self.execute_test_list_cases(self.cases_invalid_size)

    def set_formulary(self, formulary):
        self.formulary = formulary

    def populate_form_data(self,item):
        form_data = flatten_to_dict(self.formulary())
        for field in item['fields_value']:
            form_data[field] = item['fields_value'][field]
        return form_data

    def execute_test_list_cases(self, list_cases):
        for item in list_cases:
            form_data = self.populate_form_data(item)
            form = self.formulary(data=form_data)
            result = form.is_valid()
            self.assertEquals(form.is_valid(), item['expected_result'], item['success_message'])


class PasswordFormTests(TestAbstractForm):

    def __init__(self, *args, **kwargs):
        super(PasswordFormTests,self).__init__()
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.set_formulary(FormAbstractPassword)

        self.add_case_invalid_format({'password':None}, "Test null password values (OK)")
        self.add_case_invalid_format({'password': ""}, "Test empty password values (OK)")
        self.add_case_invalid_format({'password':'1234567890'},"Test passwords only numerics (OK)")
        self.add_case_invalid_format({'password':'qweasdzxcp'},"Test passwords letters (OK)")
        self.add_case_invalid_format({'password':'!@#$%¨&*()'},"Test password only symbols (OK)")

        self.add_case_valid_format({'password':'1q2w3e4r5t'}, "Test valid format password values (OK)")

        self.add_case_invalid_size({'password': '1q2'}, "Test short password values (OK)")
        self.add_case_invalid_size({'password': '1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t'}, "Test greater password values (OK)")
        self.add_case_valid_size({'password': '1q2w3e4r5t'}, "Test valid size password values (OK)")


class ConfirmPasswordFormTests(TestAbstractForm):
    def __init__(self, *args, **kwargs):
        super(ConfirmPasswordFormTests, self).__init__()
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.set_formulary(FormAbstractConfirmPassword)

        self.add_case_invalid_format({'confirm_password': None}, "Test null confirm password values (OK)")
        self.add_case_invalid_format({'confirm_password': ""}, "Test empty confirm password values (OK)")
        self.add_case_invalid_format({'confirm_password': '1234567890'}, "Test confirm passwords only numerics (OK)")
        self.add_case_invalid_format({'confirm_password': 'qweasdzxcp'}, "Test confirm passwords letters (OK)")
        self.add_case_invalid_format({'confirm_password': '!@#$%¨&*()'}, "Test confirm password only symbols (OK)")

        self.add_case_valid_format({'confirm_password': '1q2w3e4r5t'}, "Test valid format confirm password values (OK)")

        self.add_case_invalid_size({'confirm_password': '1q2'}, "Test short confirm password values (OK)")
        self.add_case_invalid_size({'confirm_password': '1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t'},"Test greater confirm password values (OK)")
        self.add_case_valid_format({'confirm_password': '1q2w3e4r5t'}, "Test valid size confirm password values (OK)")


class EmailFormTests(TestAbstractForm):
    def __init__(self, *args, **kwargs):
        super(EmailFormTests, self).__init__()
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.set_formulary(FormAbstractEmail)

        self.add_case_invalid_format({'email': None}, "Test null email values (OK)")
        self.add_case_invalid_format({'email': ""}, "Test empty email values (OK)")
        self.add_case_invalid_format({'email': '@teste.com'}, "Test email without user email (OK)")
        self.add_case_invalid_format({'email': 'teste2@.com'}, "Test email without domain (OK)")
        self.add_case_invalid_format({'email': 'teste2@teste@.com'}, "Test email with two '@' character (OK)")
        self.add_case_invalid_format({'email': 'teste2.com'}, "Test email without '@' character (OK)")
        self.add_case_invalid_format({'email': 'teste+001@gmail.com'}, "Test email with dangerous symbols (OK)")

        self.add_case_valid_format({'email': 'teste@teste.com'}, "Test valid format email values (OK)")
        self.add_case_valid_format({'email': 'teste_testes@teste.com'}, "Test valid format email with '_' character (OK)")
        self.add_case_valid_format({'email': 'teste5@teste.com'}, "Test valid format email with number (OK)")
        self.add_case_valid_format({'email': '10teste@teste.com'}, "Test valid format email initialized by with number (OK)")

        big_value_email = '1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t@1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t1q2w3e4r5t.com.br'
        self.add_case_valid_size({'email': 'teste@teste.com'},"Test email with normal size values (OK)")
        self.add_case_invalid_size({'email': big_value_email}, "Test email with exceded size values (OK)")



del(TestAbstractForm)

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





