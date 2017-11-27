from modules.entity.models import *
from django.core import serializers
import json


def create_simple_valid_person():
    entity = Entity()
    entity.entity_type = '1'
    entity.cpf_cnpj = '12859855750'
    entity.entity_name = 'PESSOA FISICA DE TESTE'
    entity.fantasy_name = 'PESSOA DE TESTE'
    return format_serialized_model(entity)

def create_simple_valid_company():
    dicionario_test = {'entity_type': ['2'], 'cpf_cnpj': ['75328405000152'], 'entity_name': ['EMPRESA XYZ'],
                  'fantasy_name': ['XYZ'], 'birth_date_foundation': [''], 'natureza_juridica': [''],
                  'main_activity': [''], 'comments': [''], 'tributary_regime': ['0'], 'entity_father': [''],
                  'entity_mother': [''], 'entity_conjuge': [''], 'entity_occupation': [''],
                  'comments_fiscal_note': ['']}
    return dicionario_test

def create_simple_person(entity_type,cpf_cnpj,entity_name,fantasy_name):
    dicionario_test = {'entity_type': [entity_type], 'cpf_cnpj': [cpf_cnpj], 'entity_name': [entity_name],
                  'fantasy_name': [fantasy_name], 'birth_date_foundation': [''], 'natureza_juridica': [''],
                  'main_activity': [''], 'comments': [''], 'tributary_regime': ['0'], 'entity_father': [''],
                  'entity_mother': [''], 'entity_conjuge': [''], 'entity_occupation': [''],
                  'comments_fiscal_note': ['']}
    return dicionario_test

def create_simple_valid_contac():
    dicionario_campos = {'entity': None, 'type_contact': ['2'], 'name': ['LUCAS'], 'ddd': ['27'], 'phone': ['30304040']
        , 'complemento': ['TESTE TESTE'], 'details': [''], 'history':[''], 'id': ['']}
    return dicionario_campos

def create_simple_valid_email():
    email = Email()
    email.name = 'Test'
    email.email = 'teste@teste.com'
    email.send_suitcase = True
    email.send_xml = True
    return email

def create_simple_invalid_company ():
    dicionario_test = {'entity_type': ['2'], 'cpf_cnpj': ['75328400000000'], 'entity_name': ['EMPRESA XYZ'],
                       'fantasy_name': ['XYZ'], 'birth_date_foundation': [''], 'natureza_juridica': [''],
                       'main_activity': [''], 'comments': [''], 'tributary_regime': ['0'], 'entity_father': [''],
                       'entity_mother': [''], 'entity_conjuge': [''], 'entity_occupation': [''],
                       'comments_fiscal_note': ['']}
    return (dicionario_test)

def format_serialized_model(object,list_fields=None):
    if list_fields is not None:
        response_model = serializers.serialize('json', [object], fields=tuple(list_fields))
    else:
        response_model = serializers.serialize('json', [object])

    response_model = json.loads(response_model)[0]
    response_model = response_model['fields']
    response_model['id'] = object.id
    return response_model