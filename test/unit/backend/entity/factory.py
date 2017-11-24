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
    entity = Entity()
    entity.entity_type = '2'
    entity.cpf_cnpj = '03853896000140'
    entity.entity_name = 'EMPRESA DE TESTES LTDA'
    entity.fantasy_name = 'EMPRESA DE TESTE'
    return format_serialized_model(entity)

def create_simple_valid_contac():
    contact = Contact()
    contact.type_contact = 2
    contact.phone = '30304040'
    contact.ddd = '27'
    contact.complemento = 'TESTE TESTE'
    return contact

def create_simple_valid_email():
    email = Email()
    email.name = 'Test'
    email.email = 'teste@teste.com'
    email.send_suitcase = True
    email.send_xml = True
    return email

def create_simple_invalid_company ():
    entity = Entity()
    entity.entity_type = '1'
    entity.cpf_cnpj = '03853896000140'
    entity.entity_name = 'EMPRESA DE TESTES LTDA'
    entity.fantasy_name = 'EMPRESA DE TESTE'
    return format_serialized_model(entity)

def format_serialized_model(object,list_fields=None):
    if list_fields is not None:
        response_model = serializers.serialize('json', [object], fields=tuple(list_fields))
    else:
        response_model = serializers.serialize('json', [object])

    response_model = json.loads(response_model)[0]
    response_model = response_model['fields']
    response_model['id'] = object.id
    response_model['selected'] = ''
    return response_model