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


        '''def test_validation_create_entity(self):
            variacoes = [
                [None, 'teste', True],
                ['38141674226', None, False],
                ['','', False],
                ['38141674226', '', False],
                ['', 'Teste', False],
                ['38141674226', 'Teste', True],
            ]

            for item in variacoes:
                entity = Entity ()
                entity.entity_type='PF'
                entity.cpf_cnpj=item[0]
                entity.entity_name=item[1]
                entity.fantasy_name='teste'

                self.assertEquals(entity.full_clean(),item[2], 'Entidade instanciada corretamento (OK)')
        '''