import json
from django.test import TestCase, Client
from django.db import transaction
from modules.entity.api import EntityController
from modules.entity.models import Entity, Contact, Email
from modules.user.models import User
from test.unit.backend.entity.factory import *


class EntityTest(TestCase, EntityController):
    #Função de LOGIN, testes precisam de simular log, para não dar error
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_test_user(email='teste@teste.com',senha='1q2w3e4r')
        print("Veja o user:",self.user, self.user.account_activated)
        response = self.c.post('/api/user/login/autentication', data={'email': self.user.email, 'password': '1q2w3e4r'},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        print(response.content)
        print("Consigo acessar? ",response)

    #Função que cria para o test uma entidade valida
    def create_entity (self):
        entity = create_simple_valid_company()
        entity.pop('id', None)
        self.c.post('/api/entity/save', data=entity)

    #Tests Entity
    def test_create_entity(self):
        try:
            entity = Entity()
            self.assertTrue(isinstance(entity, Entity), 'ontato instanciada corretamente (OK)')
            self.assertEquals(entity.__unicode__(), entity.cpf_cnpj,"Representacao do objeto com unicode (OK)")
        except:
            entity = None
            self.assertIsNone(entity,"Entidade Não criada (OK)")

    def test_validation_create_entity(self):
        variacoes = [
            ['', '', False],
            ['', 'Teste', False],
            [None, 'teste', False],
            ['81575080967', '', False],
            ['81575080967', None, False],
            ['81575080966', 'TESTE', False],
        ]

        for item in variacoes:
            entity = create_simple_person('1',item[0],item[1],'teste teste')
            entity.pop('id', None)
            try:
                obj = self.c.post('/api/entity/save', data=entity)
                result = json.loads(obj.content)
            except Exception as exception:
                result = {}
                result['result'] = False
            self.assertEquals(result['result'], item[2],"Teste de criacao (OK)")

    def test_create_entity_wrong_document(self):
        entity = create_simple_invalid_company()
        entity.pop('id',None)
        try:
            obj = self.c.post('/api/entity/save', data=entity)
            result = json.loads(obj.content)
        except Exception as exception:
            result = {}
            result['result'] = False
        self.assertEquals(result['result'], False, "Teste de criacao de entidade com documento incorreto para o seu tipo (PF ou PJ). (OK)")

    def test_create_entity_correct_document(self):
        entity = create_simple_valid_company()
        entity.pop('id',None)
        try:
            obj = self.c.post('/api/entity/save', data=entity)
            result = json.loads(obj.content)
        except Exception as exception:
            result = {}
            result['result'] = False
        self.assertEquals(result['result'], True, "Teste de criacao de entidade com documento correto para o seu tipo (PF ou PJ). (OK)")


    #Tests Entity->Contact
    def test_create_entity_contact (self):
        try:
            contact = Contact()
            self.assertTrue(isinstance(contact, Contact), 'Entidade instanciada corretamente (OK)')
            #self.assertEquals(contact.__unicode__(), contact.cpf_cnpj,"Representacao do objeto com unicode (OK)")
        except:
            entity = None
            self.assertIsNone(entity,"Entidade Não criada (OK)")

    def test_validation_create_entity_contact(self):
        self.create_entity()
        variacoes = [
            ['','',False],
            [None,None,False],
            ['123456789','',False],
            ['','27',False],
            ['12345678AA','27',False],
            ['123456789','A27',False],
            ['123456789','27',True]
        ]
        entity = Entity.objects.get(id=1)
        contact = create_simple_valid_contac()
        contact.pop('id',None)
        contact['entity_id'] = entity.id
        for item in variacoes:
            contact['phone'] = item[0]
            contact['ddd'] = item[1]
            try:
                obj = self.c.post('/api/entity/register/contact', data=contact)
                result = json.loads(obj.content)
            except Exception as exception:
                result = {}
                result['result'] = False
            self.assertEquals(result['result'],item[2],"Teste de criação (OK)")

    def test_create_entity_valid_contact(self):
        self.create_entity()
        entity = Entity.objects.get(id=1)
        contact = create_simple_valid_contac()
        contact.pop('id', None)
        contact['entity_id'] = entity.id
        try:
            obj = self.c.post('/api/entity/register/contact', data=contact)
            result = json.loads(obj.content)
        except Exception as exception:
            result = {}
            result['result'] = False
        self.assertEquals(result['result'], True, "Teste Criação de uma Contato Telefonico valido para uma Entidade. (OK)")

    def test_create_entity_wrong_cotact(self):
        self.create_test_entity()
        entity = Entity.objects.get(id=1)
        contact = create_simple_valid_contac()
        contact.pop('id', None)
        contact['phone'] = '3030AA30'
        contact['entity_id'] = entity.id
        try:
            obj = self.c.post('/api/entity/register/contact', data=contact)
            result = json.loads(obj.content)
        except Exception as exception:
            result = {}
            result['result'] = False
        self.assertEquals(result['result'], False, "Teste de criacao de Contato Telefonico. (OK)")


    #Testes Entity-Email
    def test_create_entity_email(self):
        try:
            email = Email()
            self.assertTrue(isinstance(email,Email), 'Contato instanciada corretamente (OK)')

        except:
            entity = None
            self.assertIsNone(entity, "Entidade Não criada (OK)")

    def test_validation_create_entity_email(self):
        self.create_entity()
        entity = Entity.objects.get(id=1)
        variacoes = [
            [None, True, 'gianordolilucas@gmail.com', False],
            [True, None, 'gianordolilucas@gmail.com', False],
            ['', False, 'gianordolilucas@gmail.com', False],
            [False, '', 'gianordolilucas@gmail.com', False],
            [False, True, None, False],
            [True, True, '', False],
            [False, False, 'teste@', False],
            [False, False, '@.com', False],
            [False, False, 'teste_teste@@.com', False],
            [True, True, 'gianordolilucas@gmail.com', True],
            [False, False, 'gianordolilucas@gmail.com', True]
        ]

        for item in variacoes:
            email = create_simple_valid_email()
            email.pop('id', None)
            email['email'] = item[2]
            email['send_xml'] = item[0]
            email['send_suitcase'] = item[1]
            email['entity_id'] = entity.id
            try:
                obj = self.c.post('/api/entity/register/email', data=email)
                result = json.loads(obj.content)
            except Exception as exception:
                result = {}
                result['result'] = False
            self.assertEquals(result['result'],item[3],"Teste de criação (OK)")

    def test_create_entity_valid_email(self):
        self.create_entity()
        entity = Entity.objects.get(id=1)
        email = create_simple_valid_email()
        email.pop('id', None)
        email['entity_id'] = entity.id
        try:
            obj = self.c.post('/api/entity/register/email', data=email)
            result = json.loads(obj.content)
        except Exception as exception:
            result = {}
            result['result'] = False
        self.assertEquals(result['result'], True, "Teste de criacao de Contato de Email. (OK)")

    def test_create_entity_wrong_email(self):
        self.create_entity()
        entity = Entity.objects.get(id=1)
        email = create_simple_valid_email()
        email.pop('id', None)
        email['entity_id'] = entity.id
        email['email'] = '>@.com'
        try:
            obj = self.c.post('/api/entity/register/email', data=email)
            result = json.loads(obj.content)
        except Exception as exception:
            result = {}
            result['result'] = False
        self.assertEquals(result['result'], False, "Teste de criacao de Contato de um Email Inválido. (OK)")