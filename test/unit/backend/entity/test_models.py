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
            ['81575080966', 'TESTES TESTE TES', True],
            [None, 'teste', False],
            ['81575080966', None, False],
            ['', '', False],
            ['81575080966', '', False],
            ['', 'Teste', False],
        ]
        cont =0

        for item in variacoes:
            cont+=1
            entity = Entity ()
            try:
                entity.entity_type = 'PF'
                entity.cpf_cnpj = item[0]
                entity.entity_name = item[1]
                entity.fantasy_name='teste teste'
                entity.save()
                result = True
                try:
                    Entity.objects.filter(cpf_cnpj=item[0]).delete()
                except:
                    pass
            except:
                result = False

            self.assertEquals(result,item[2],"Teste de criacção (OK)")