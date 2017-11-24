from django.test import TestCase, Client
from django.db import transaction
from modules.entity.api import EntityController
from modules.entity.models import Entity, Contact, Email
from modules.user.models import User
from test.unit.backend.entity.factory import create_simple_valid_company, create_simple_valid_contac, \
    create_simple_valid_person, create_simple_valid_email, create_simple_invalid_company


class EntityTest(TestCase, EntityController):

    def setUp(self):
        self.c = Client()
        user = User.objects.create_test_user(email='teste@teste.com',senha='1q2w3e4r')
        print("Veja o user:",user, user.account_activated)
        response = self.c.post('/api/user/login/autentication', data={'email': user.email, 'password': '1q2w3e4r'},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        print("Consigo acessar? ",response)

    def request (self,url,dict):
        response = self.c.post(url,dict)
        return response


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
            ['81575080966', 'TESTE', True],
            ['81575080966', 'TESTE', False],
        ]

        for item in variacoes:
            #print("VOU TESTAR OS VALORES: (",item[0],") e (",item[0],")")
            entity = Entity()
            entity.entity_type = 'PF'
            entity.cpf_cnpj = item[0]
            entity.entity_name = item[1]
            entity.fantasy_name = 'teste teste'
            try:
                EntityController.save(entity)
                result = True
            except Exception as exception:
                #print("ERRO: ",exception)
                result = False

            #if result:
            #    Entity.objects.filter(cpf_cnpj=item[0]).delete()

            #print("V1:",item[0]," - V2:",item[1]," - RESP.:",item[2]," - RESULT:",result)
            self.assertEquals(result,item[2],"Teste de criação (OK)")

    def test_create_entity_wrong_document(self):
        entity = create_simple_invalid_company()
        request = self.request('/api/entity/save',entity)
        result = True
        try:
            EntityController().save(request)
            result = True
        except Exception as exception:
            #print("ERRO: ",exception)
            result = False
        self.assertEquals(result, False, "Teste de criacao de entidade com documento incorreto para o seu tipo (PF ou PJ). (OK)")

    def test_create_entity_correct_document(self):
        entity = create_simple_valid_company()
        print("Olha o Entity:",entity)
        request = self.request('/api/entity/save', entity)
        print("Olha o request:",request)
        print("Veja a resposta:",request.status_code)
        result = True
        try:
            EntityController().save(request)
            result = True
        except Exception as exception:
            #print("ERRO: ",exception)
            result = False
        self.assertEquals(result, True, "Teste de criacao de entidade com documento correto para o seu tipo (PF ou PJ). (OK)")


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
        entity = create_simple_valid_person()
        EntityController.save(entity)
        variacoes = [
            ['','',False],
            [None,None,False],
            ['123456789','',False],
            ['','27',False],
            ['12345678AA','27',False],
            ['123456789','A27',False],
            ['123456789','27',True]
        ]

        for item in variacoes:

            #print("VOU TESTAR OS VALORES: (",item[0],") e (",item[0],")")
            contact = Contact()
            contact.type_contact = 'TEST'
            contact.name = 'TESTE CONTACT'
            contact.phone = item[0]
            contact.ddd = item[1]
            contact.complemento = 'teste teste'
            contact.entity = entity
            try:
                with transaction.atomic():
                    contact.save()
                    result = True
            except Exception as exception:
                contact.active = False
                #print("ERRO: ",exception)
                result = False
            self.assertEquals(result,item[2],"Teste de criação (OK)")

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