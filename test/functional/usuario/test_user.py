from unittest import TestCase
from sistemaweb.settings import SELENIUM_URL_PROJECT_TEST
from test.functional.selenium_controller.web_controller import DjangoWebTest

class UserTest(TestCase):

    def test_create_user(self):
        web_client = DjangoWebTest(SELENIUM_URL_PROJECT_TEST)
        web_client.register('gianordolilucas@gmail.com','1q2w3e4r','1q2w3e4r')
        #web_client.login('gianordolilucas@gmail.com','1q2w3e4r')

        if self.assertEqual(web_client.get_title(),"SistemaWeb - Login", "Test login page"):
            web_client.close()