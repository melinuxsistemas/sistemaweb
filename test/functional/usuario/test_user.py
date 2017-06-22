import time
from unittest import TestCase

from modules.usuario.models import Usuario
from sistemaweb.settings import SELENIUM_URL_PROJECT_TEST
from test.functional.selenium_controller.web_controller import DjangoWebTest

class UserTest(TestCase):

    web_client = None

    def setUp(self):
        if self.web_client is None:
            self.web_client = DjangoWebTest(SELENIUM_URL_PROJECT_TEST)

    def test_register_user(self):
        self.web_client.register('test@gmail.com','1q2w3e4r','1q2w3e4r')

        while self.web_client.get_title() == 'SistemaWeb - Novo Usuário':
            time.sleep(4)
            continue
        self.assertEquals(self.web_client.get_title(),'SistemaWeb - Verifique seu Email','Test register confirmation page (OK)')
        self.web_client.excluir_usuario('test@gmail.com')
        self.web_client.close()

    def test_login(self):
        self.web_client.login('gianordolilucas@gmail.com', '1q2w3e4r')
        while self.web_client.get_title() == 'Sistemaweb - Login':
            time.sleep(4)
            continue
        time.sleep(2)
        self.assertEquals(self.web_client.get_title(),'Sistemaweb - Base Page', 'Test login register (OK)')
    '''
    def test_trocar_senha (self):
        self.web_client.trocar_senha('gianordolilucas@gmail.com', '1q2w3e4r', 'abcd1234', 'abcd1234')
        

        self.web_client.logout()
        self.assertEquals(self.web_client.get_title(),'SistemaWeb - Login', 'Test Troca senha (OK)')
        self.web_client.trocar_senha('gianordolilucas@gmail.com', 'abcd1234', '1q2w3e4r', '1q2w3e4r')
        self.web_client.logout()
        self.assertEquals(self.web_client.get_title(), 'SistemaWeb - Login', 'Test Troca senha (OK)')
    '''








        #web_client.login('gianordolilucas@gmail.com','1q2w3e4r')
        #web_client.trocar_senha('gianordolilucas@gmail.com','159753lucas','1q2w3e4r','1q2w3e4r')
        #if self.assertEqual(web_client.get_title(),"SistemaWeb - Login", "Test login page"):
        #    web_client.close()
