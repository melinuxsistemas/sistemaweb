import unittest
from test.unit.backend.core.test_routes import BaseRoutesTests, StatusCode


class EntityRoutesTests(BaseRoutesTests):

    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)

        self.add_public_route_list([])
        #self.add_private_route_list(['api/entity/register/person'])
        #self.add_private_api('api/entity/register/person/save',{'entity_type': 'PF', 'cpf_cnpj': '12859855750', 'entity_name': 'TESTE TESTE'})


    """
    def test_valid_activation_page(self):
        test_user = User.objects.create_test_user('outroteste@teste.com.br', '1q2w3e4r')
        activation_code = test_user.activation_code
        test_user.activation_code = None
        test_user.account_activated = False
        test_user.save()
        if test_user is not None:
            activation_code_route = '/register/activate/'+test_user.email+'/'+activation_code+"/"
            response = self.client.get(activation_code_route)
            self.assertEqual(response.status_code, StatusCode.request_redirected)
        test_user.delete()

    def test_invalid_activation_code_page(self):
        test_user = User.objects.create_test_user('teste@teste.com.br', '1q2w3e4r')
        if test_user is not None:
            activation_code_route = '/register/activate/' + test_user.email + '/10b9271023120060e584492f48557272e2c313ae1451b1/'
            response = self.client.get(activation_code_route)
            self.assertEqual(response.status_code, StatusCode.request_success)
        test_user.delete()

    def test_invalid_activation_email_page(self):
        activation_code_route = '/register/activate/' + 'testeteste.com.br' + '/10b9271023120060e584492f48557272e2c313ae1451b1/'
        response = self.client.get(activation_code_route)
        self.assertEqual(response.status_code, StatusCode.request_success)

    def test_invalid_non_registered_email_page(self):
        test_user = User.objects.create_test_user('teste@teste.com.br', '1q2w3e4r')
        if test_user is not None:
            activation_code_route = '/register/activate/teste@outroteste.com/'+test_user.activation_code+"/"
            response = self.client.get(activation_code_route)
            self.assertEqual(response.status_code, StatusCode.request_success)
        test_user.delete()

    def test_reset_password_valid_email(self):
        test_user = User.objects.create_test_user('teste@teste.com.br', '1q2w3e4r')
        response = self.client.post('/api/user/reset_password',data={'email':test_user.email})
        self.assertEqual(json.loads(response.content)['success'] , True)
        self.assertEqual(response.status_code, StatusCode.request_success)
        test_user.delete()

    def test_reset_password_without_email(self):
        response = self.client.post('/api/user/reset_password', data={})
        self.assertEqual(json.loads(response.content)['success'], False)
        self.assertEqual(response.status_code, StatusCode.request_success)

    def test_reset_password_with_empty_email(self):
        response = self.client.post('/api/user/reset_password', data={'email':''})
        self.assertEqual(json.loads(response.content)['success'], False)
        self.assertEqual(response.status_code, StatusCode.request_success)

    def test_reset_password_with_invalid_email(self):
        response = self.client.post('/api/user/reset_password', data={'email': 'teste.com.br'})
        self.assertEqual(json.loads(response.content)['success'], False)
        self.assertEqual(response.status_code, StatusCode.request_success)

    def test_reset_password_with_inexist_user(self):
        response = self.client.post('/api/user/reset_password', data={'email': 'teste@teste.com.br'})
        self.assertEqual(json.loads(response.content)['success'], False)
        self.assertEqual(response.status_code, StatusCode.request_success)

    def test_resend_activation_valid_email(self):
        test_user = User.objects.create_contracting_user('teste@teste.com.br', '1q2w3e4r')
        response = self.client.post('/api/user/reactivate', data={'email': test_user.email})
        self.assertEqual(json.loads(response.content)['success'], True)
        self.assertEqual(response.status_code, StatusCode.request_success)
        test_user.delete()

    def test_resend_activation_without_email(self):
        response = self.client.post('/api/user/reactivate', data={})
        self.assertEqual(json.loads(response.content)['success'], False)
        self.assertEqual(response.status_code, StatusCode.request_success)

    def test_resend_activation_empty_email(self):
        response = self.client.post('/api/user/reactivate', data={'email': ''})
        self.assertEqual(json.loads(response.content)['success'], False)
        self.assertEqual(response.status_code, StatusCode.request_success)

    def test_resend_activation_invalid_email(self):
        response = self.client.post('/api/user/reactivate', data={'email': 'testeteste.com.br'})
        self.assertEqual(json.loads(response.content)['success'], False)
        self.assertEqual(response.status_code, StatusCode.request_success)

    def test_resend_activation_inexist_email(self):
        response = self.client.post('/api/user/reactivate', data={'email': 'teste@teste.com.br'})
        self.assertEqual(json.loads(response.content)['success'], False)
        self.assertEqual(response.status_code, StatusCode.request_success)
    """