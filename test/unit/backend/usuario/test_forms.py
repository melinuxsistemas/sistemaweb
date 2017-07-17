import unittest

from modules.user.forms import FormChangePassword, FormLogin, FormRegister
from test.unit.backend.core.test_forms import TestAbstractForm


class ChangePasswordFormTest (TestAbstractForm):
    def __init__(self, *args, **kwargs):
        super(ChangePasswordFormTest, self).__init__()
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.set_formulary(FormChangePassword)

        #Valors de tamanho invalido
        self.add_case_invalid_size({'old_password': 'abcd1234', 'password': '', 'confirm_password': ''}, "Test empyt size is invalid (OK)")
        self.add_case_invalid_size({'old_password': '1234abcd', 'password': '123', 'confirm_password': 'abdc1234'}, "Test new password is invalid (OK)")
        self.add_case_invalid_size({'old_password': '1234abcd', 'password': 'abcd1234', 'confirm_password': '123'}, "Test new confirm password is invalid (OK)")

        #valores de formato invalido
        self.add_case_invalid_format({'old_password':'abdc1234', 'password': None , 'confirm_password':None }, "Test newp password is invalid (OK)")
        self.add_case_invalid_format({'old_password':'1234abcd', 'password':'12345678', 'confirm_password': 'abdc1234'}, "Test new password is invalid (OK)")
        self.add_case_invalid_format({'old_password': '1234abcd', 'password': '!1@2#3$4%5', 'confirm_password': 'abdc1234'},"Test new password is invalid (OK)")
        self.add_case_invalid_format({'old_password': '1234abcd', 'password': 'abdc1234', 'confirm_password': '1@2#3$4%5'},"Test new confirm password is invalid (OK)")
        self.add_case_invalid_format({'old_password': '1234abcd', 'password': '1234abcd', 'confirm_password': '1234abcd'},"Test new_password and confirm_new_password is equal to old_passwaod (OK)")
        self.add_case_invalid_format({'old_password': '1234abcd', 'password': '1234abcd', 'confirm_password': '1a2b3c4d'},"Test new_password and confirm_new_password is not equal(OK)")

        #valor de formato e tamanho valido
        self.add_case_valid_format({'old_password': '1234abcd', 'password': 'abcd1234', 'confirm_password': 'abcd1234'},"Test change password is valid (OK)")


class LoginFormTest (TestAbstractForm):

    def __init__(self, *args, **kwargs):
        super(LoginFormTest, self).__init__()
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.set_formulary(FormLogin)

        #Valores invalidos
        self.add_case_invalid_format({'email': None, 'password': None,}, "Test email and password are Null Value (OK)")
        self.add_case_invalid_format({'email': '','password': ''}, "Test email and password are empty string (OK)")
        self.add_case_invalid_format({'email': 'MuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrandeMuitoGrande@gmail.com', 'password': '1234abcd'}, "Test email is very large (OK)")
        self.add_case_invalid_format({'email': 'teste@teste@gmail.com', 'password': '1234abcd'}, "Test email have two or more '@' (OK)")
        self.add_case_invalid_format({'email': 'testa@test', 'password': '1234abcd'}, "Test email have . something (OK)")
        self.add_case_invalid_format({'email': 'teste@teste.com', 'password': 'SenhaGrandeSenhaGrandeSenhaGrandeSenhaGrandeSenhaGrandeSenhaGrande'}, "Test password is very large (OK)")

        #Valores de Campos aceitos
        self.add_case_valid_format({'email': 'Teste@test.com','password': '1234abcd'},"Email and Password are valid (OK)")


class FormRegisterTest (TestAbstractForm):

    def __init__(self, *args, **kwargs):
        super(FormRegisterTest, self).__init__()
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.set_formulary(FormRegister)

        #Valores de tamanho Invalidos:
        self.add_case_invalid_size({'email': 'test@test.com', 'password': '123', 'confirm_password': '123'},"Test password and confirm_new_password are too small (OK)")
        self.add_case_invalid_size({'email': '', 'password': 'test1234', 'confirm_password': 'test1234'}, "Test email is empty (OK")
        self.add_case_invalid_size({'email': 'test@test.com', 'password': '', 'confirm_password': ''}, "Test password and confirm_passwor are empty (OK")

        #Valores de formato Invalido:
        self.add_case_invalid_format({'email': None, 'password': None, 'confirm_password': None}, "Test all fields are Null value (OK")
        self.add_case_invalid_format({'email': 'test@test.com', 'password': None, 'confirm_password': None}, "Test password and confirm_password are Null value (OK")
        self.add_case_invalid_format({'email': 'teste@@test.com', 'password': 'test1234', 'confirm_password': 'test1234'}, "Test Email is inValid (OK")
        self.add_case_invalid_format({'email': 'teste@test.com', 'password': 'test1234', 'confirm_password': '1234test'}, "Test Password is different from confirm_password(OK")

        #Formato Valido:
        self.add_case_valid_format({'email': 'teste@test.com', 'password': 'test1234', 'confirm_password': 'test1234'},"All fields are equals (OK")