from django.test import RequestFactory, TestCase
from modules.entity.models import Entity
from datetime import datetime
from modules.entity.views import register_entity


class SimpleTest (TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.entity = Entity.objects.create(
            cpf_cnpj = '149.601.757-96',
            entity_name = 'Teste Teste',
            fantasy_name = 12348,
            birth_date_foundation = datetime.now(),

        )

    def test_details(self):

        request = self.factory.post('/entity/register/person/')
        request.user = self.entity
        response = register_entity(request,'person')
        self.assertEqual(response.status_code, 200)