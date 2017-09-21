from django.test import TestCase
from test.unit.backend.core.test_routes import NewBaseRoutesTest


class EntityRoutesTest(TestCase, NewBaseRoutesTest):
    private_routes = ['/entity/']
    private_api = []

    private_api.append(['/api/entity/register/person/save', {'entity_type': 'PF','registration_status': 0,'cpf_cnpj': '12859855750',
            'entity_name': 'TESTE TESTE','fantasy_name': '','birth_date_foundation': '','comments': ''}])


"""
class BaseRoutesTest:

    def __init__(self, unittest_class):
        self.unittest_class = unittest_class



class ControllerRoutes:

    def __init__(self, unittest_class):
        self.unittest_class = unittest_class

    def add_private_route(self, route):
        self.private_routes.append(route)

    def add_private_route_list(self, list_routes):
        self.private_routes = self.private_routes + list_routes

    #def test_private_routes_autenticated_user(self):
    #    self.base_class.assertEqual(30, 20)

class BaseRoutesTests:

    private_routes = []
    public_routes = []

    def __init__(self, unittest_class, *args, **kwargs):
        self.routes_test_cases = BaseRoutesTest(unittest_class)
        self.controller_routes = ControllerRoutes(unittest_class)
        
    def test_private_routes(self):
        self.routes_test_cases.test_private_routes_anonymous_user(self.private_routes)
        #self.routes_test_cases.test_private_routes_autenticated_user(self.private_routes)

    #def test_private_routes_anonymous(self):
    #    for item in self.private_routes:
    #        self.assertNotEqual(self.client.get(item).status_code, StatusCode.request_success)


class EntityRoutesTest(TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        test = BaseRoutesTests(self)


"""





"""
class BaseRoutesTests(TestCase):
    public_routes = []
    private_routes = []

    public_api = []
    private_api = []

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        self.client = Client()

    def login_user_client(self, email, senha):
        self.user = User.objects.create_test_user(email, senha)
        self.client.login(username=email, password=senha)
        return self.user

    def add_public_route(self, route):
        self.public_routes.append(route)

    def add_public_route_list(self, list_routes):
        self.public_routes = self.public_routes + list_routes

    def add_private_route(self, route):
        self.private_routes.append(route)

    def add_private_route_list(self, list_routes):
        self.private_routes = self.private_routes + list_routes

    def add_public_api(self, api, dict_paramters):
        self.public_api.append([api,dict_paramters])

    def add_private_api(self, api, dict_paramters):
        self.private_api.append([api, dict_paramters])

    def test_get_route_list(self, route_list=[], status_code=StatusCode.request_success):
        for item in route_list:
            return_status_code = self.client.get(item).status_code
            if status_code == StatusCode.request_success:
                if return_status_code == StatusCode.request_redirected_permanently:
                    return_status_code = StatusCode.request_success
            self.assertEqual(return_status_code, status_code)

    def test_post_route_list(self, route_list=[], status_code=StatusCode.request_success):
        for item in route_list:
            result = self.client.post(item[0], data=item[1], HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            self.assertEqual(result.status_code,status_code)

    def test_public_routes(self):
        self.test_get_route_list(self.public_routes, StatusCode.request_success)

    def test_private_routes_autenticated(self):
        user = self.login_user_client('teste@teste.com', '1q2w3e4r')
        self.test_get_route_list(self.private_routes, StatusCode.request_success)
        user.delete()

    def test_private_routes_anonymous(self):
        for item in self.private_routes:
            self.assertNotEqual(self.client.get(item).status_code, StatusCode.request_success)

    def test_get_private_api(self):
        self.test_get_route_list(self.private_api, StatusCode.request_not_found)

    def test_post_private_api(self):
        user = self.login_user_client('teste@teste.com', '1q2w3e4r')
        self.test_post_route_list(self.private_api, StatusCode.request_success)
        user.delete()

    def test_get_public_api(self):
        for item in self.public_api:
            response = self.client.get(item[0],data=item[1])
            self.assertNotEqual(response.status_code, StatusCode.request_success)


class EntityRoutesTests(BaseRoutesTests):

    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)

        self.add_public_route_list([])
        self.add_private_route_list(['/entity/register/person'])
        self.add_private_route_list(['/entity/register/company'])

        test_paramters = {'entity_type':'PF',
            'registration_status': 0,
            'cpf_cnpj': '12859855750',
            'entity_name': 'TESTE TESTE',
            'fantasy_name': '',
            'birth_date_foundation': '',
            'comments': ''
        }

        self.add_private_api('/api/entity/register/person/save',test_paramters)
"""





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