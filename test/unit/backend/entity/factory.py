from modules.entity.models import Entity


def create_simple_valid_person():
    entity = Entity()
    entity.entity_type = 'PF'
    entity.cpf_cnpj = '12859855750'
    entity.entity_name = 'PESSOA FISICA DE TESTE'
    entity.fantasy_name = 'PESSOA DE TESTE'
    return entity

def create_simple_valid_company():
    entity = Entity()
    entity.entity_type = 'PJ'
    entity.cpf_cnpj = '03853896000140'
    entity.entity_name = 'EMPRESA DE TESTES LTDA'
    entity.fantasy_name = 'EMPRESA DE TESTE'
    return entity