from modules.entity.models import *
from django.core import serializers
import json

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
    email = {'email': ['teste@teste.com'], 'name': ['TESTE'], 'entity': None, 'send_xml': False, 'send_suitcase': True,
             'details': [''], 'history': [''], 'id': ['1']}
    return email

def create_simple_invalid_company ():
    dicionario_test = {'entity_type': ['2'], 'cpf_cnpj': ['75328400000000'], 'entity_name': ['EMPRESA XYZ'],
                       'fantasy_name': ['XYZ'], 'birth_date_foundation': [''], 'natureza_juridica': [''],
                       'main_activity': [''], 'comments': [''], 'tributary_regime': ['0'], 'entity_father': [''],
                       'entity_mother': [''], 'entity_conjuge': [''], 'entity_occupation': [''],
                       'comments_fiscal_note': ['']}
    return (dicionario_test)
