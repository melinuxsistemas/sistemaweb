import json
from django.test import TestCase, Client
from django.db import transaction
from modules.entity.api import EntityController
from modules.entity.models import Entity, Contact, Email
from modules.user.models import User
from test.unit.backend.entity.factory import create_simple_valid_company, create_simple_valid_contac, \
    create_simple_valid_person, create_simple_valid_email, create_simple_invalid_company, create_simple_person


class EntityTest(TestCase, EntityController):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_test_user(email='teste@teste.com',senha='1q2w3e4r')
        print("Veja o user:",self.user, self.user.account_activated)
        response = self.c.post('/api/user/login/autentication', data={'email': self.user.email, 'password': '1q2w3e4r'},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        print(response.content)
        print("Consigo acessar? ",response)


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
        entity = create_simple_valid_company()
        entity.pop('id', None)
        obj = self.c.post('/api/entity/save', data=entity)
        result = json.loads(obj.content)
        print("Resulltadoooo:",result)
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
        print("OLHA O CONTAAAAAAAAAATO:",contact)
        contact['entity'] = entity.id

        for item in variacoes:
            #print("VOU TESTAR OS VALORES: (",item[0],") e (",item[0],")")

            try:
                contact_json = bj = self.c.post('/api/entity/register/contact', data=contact)
                cont = json.load(contact_json.content)
                print("OLHA O CONTENT:",cont)
            except Exception as exception:
                result = {}
                result['result'] = False
            self.assertEquals(result['result'],item[2],"Teste de criação (OK)")
    '''
    def test_create_entity_valid_contact(self):
        entity = create_simple_valid_person()
        EntityController.save(entity)
        contact = create_simple_valid_contac()
        contact.entity = entity
        try:
            contact.save()
            result = True
        except Exception as exception:
            #print("ERRO: ",exception)
            result = False
        self.assertEquals(result, True, "Teste Criação de uma Contato Telefonico valido para uma Entidade. (OK)")

    def test_create_entity_wrong_cotact(self):
        entity = create_simple_valid_person()
        EntityController.save(entity)
        contact = create_simple_valid_contac()
        contact.entity = entity
        contact.phone = "3030323a"
        try:
            contact.save()
            result = True
        except Exception as exception:
            #print("ERRO: ",exception)
            result = False
        self.assertEquals(result, False, "Teste de criacao de Contato Telefonico. (OK)")


    #Testes Entity-Email
    def test_create_entity_email(self):
        try:
            email = Email()
            self.assertTrue(isinstance(email,Email), 'Contato instanciada corretamente (OK)')

        except:
            entity = None
            self.assertIsNone(entity, "Entidade Não criada (OK)")

    def test_validation_create_entity_email(self):
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
            # [False, False, 'gianordolilucas@gmail.com', True]
        ]
        entity = create_simple_valid_person()
        EntityController.save(entity)

        for item in variacoes:
            email = Email()
            email.email = item[2]
            email.name = 'TESTE EMAIL'
            email.send_xml = item[0]
            email.send_suitcase = item[1]
            email.entity = entity
            try:
                with transaction.atomic():
                    email.save()
                    result = True
            except Exception as exception:
                email.active = False
                result = False
            self.assertEquals(result,item[3],"Teste de criação (OK)")

    def test_create_entity_valid_email(self):
        entity = create_simple_valid_person()
        EntityController.save(entity)
        email = create_simple_valid_email()
        email.entity = entity
        try:
            email.save()
            result = True
        except Exception as exception:
            result = False
        self.assertEquals(result, True, "Teste de criacao de Contato de Email. (OK)")

    def test_create_entity_wrong_email(self):
        entity = create_simple_valid_person()
        EntityController.save(entity)
        email = create_simple_valid_email()
        email.email = None
        email.entity = entity
        try:
            email.save()
            result = True
        except Exception as exception:
            result = False
        self.assertEquals(result, False, "Teste de criacao de Contato de um Email Inválido. (OK)")
'''