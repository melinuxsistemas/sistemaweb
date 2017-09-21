import json
from django.test import TestCase
from modules.user.models import User
from test.unit.backend.core.test_routes import NewBaseRoutesTest, StatusCode


class UserRoutesTests(TestCase, NewBaseRoutesTest):

    public_routes = ['/login/', '/logout', '/register/', '/reset_password/']
    private_route = ['/', '/profile']
    private_api   = []
    protected_api = []

    protected_api.append(['/api/user/register/save', {'email': 'teste@teste.com', 'password': '1q2w3e4r', 'confirm_password': '1q2w3e4r'}])
    protected_api.append(['/api/user/login/autentication', {'email': 'teste@teste.com', 'senha': '1q2w3e4r'}])

    private_api.append(['/api/user/change_password', {'old_password': 'r4e3w2q1', 'password': '1q2w3e4r', 'confirm_password': '1q2w3e4r'}])

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
