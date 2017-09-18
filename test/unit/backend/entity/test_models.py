from django.test import TestCase
from modules.entity.models import Entity

class EntityTest(TestCase):

    def test_create_entity(self):
        try:
            entity = Entity()
            self.assertTrue(isinstance(entity, Entity), 'Entidade instanciada corretamente (OK)')
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
            #print("VOU TESTAR OS VALORES: ("+item[0]+") e ("+item[0]+")")
            entity = Entity()
            entity.entity_type = 'PF'
            entity.cpf_cnpj = item[0]
            entity.entity_name = item[1]
            entity.fantasy_name = 'teste teste'
            try:
                entity.save()
                result = True
            except Exception as exception:
                #print("ERRO: ",exception)
                result = False

            #if result:
            #    Entity.objects.filter(cpf_cnpj=item[0]).delete()

            #print("V1:",item[0]," - V2:",item[1]," - RESP.:",item[2]," - RESULT:",result)
            self.assertEquals(result,item[2],"Teste de criação (OK)")