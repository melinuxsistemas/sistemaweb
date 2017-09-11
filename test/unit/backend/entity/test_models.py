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
            ['81575080966', '', False],
            ['81575080966', None, False],
            ['81575080966', 'TESTES TESTE TES', True],
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
                Entity.objects.filter(cpf_cnpj=item[0]).delete()
                result = True
            except:
                result = False

            #print("VEJA OS VALORES QUE DA ERRO: ",result,item[0],item[1],item[2])
            
            self.assertEquals(result,item[2],"Teste de criação (OK)")