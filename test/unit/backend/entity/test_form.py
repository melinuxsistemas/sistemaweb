from unittest import TestCase
import unittest

from modules.entity.forms import *
from test.unit.backend.core.test_forms import TestAbstractForm


class RegisterEntityFormTest (TestAbstractForm):

    def __init__(self,*args, **kwargs):
        super(RegisterEntityFormTest, self).__init__()
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.set_formulary(EntityIdentificationForm)

        #test field cpf_cnpjfreg

        #invalids
        self.add_case_invalid_format({'cpf_cnpj':None,'entity_name':'Teste teste', 'fantasy_name':'teste', 'birth_date_foundation':'10/10/1995'},"Cpf is not valid (OK)")
        self.add_case_invalid_format({'cpf_cnpj':'14960175796','entity_name': None, 'fantasy_name':'teste', 'birth_date_foundation':'10/10/1995'},"Entity name is not valid (OK)")
        self.add_case_invalid_format({'cpf_cnpj':'14960175796','entity_name': 'TesteMinWord', 'fantasy_name': None, 'birth_date_foundation':'10/10/1995'},'Entity Fantasy name is not valid (OK)')
        self.add_case_invalid_format({'cpf_cnpj': '14960175796', 'entity_name': 'TesteMinWord', 'fantasy_name': 'teste','birth_date_foundation': None}, 'Entity name is not valid (OK)')

        self.add_case_invalid_size({'cpf_cnpj': '', 'entity_name': 'Teste teste', 'fantasy_name': 'teste', 'birth_date_foundation': '10/10/1995'}, "Cpf is not valid (OK)")
        self.add_case_invalid_size({'cpf_cnpj': '14960175796', 'entity_name': '', 'fantasy_name': 'teste','birth_date_foundation': '10/10/1995'}, "Entity name is not valid (OK)")
        self.add_case_invalid_size({'cpf_cnpj': '14960175796', 'entity_name': 'TesteMinWord', 'fantasy_name': '', 'birth_date_foundation': '10/10/1995'}, 'Entity Fantasy name is not valid (OK)')
        self.add_case_invalid_size({'cpf_cnpj': '14960175796', 'entity_name': 'TesteMinWord', 'fantasy_name': 'teste','birth_date_foundation': ''}, 'Entity name is not valid (OK)')
        self.add_case_invalid_size({'cpf_cnpj': '149601757961496017579614960175796', 'entity_name': 'TesteMinWord', 'fantasy_name': 'teste','birth_date_foundation': '10/10/1995'}, 'Entity name is not valid (OK)')
        self.add_case_invalid_size({'cpf_cnpj': '14960175796', 'entity_name': 'TESTEtesteTesteTESTEtesteTesteTESTEtesteTesteTESTEtesteTesteTESTEtesteTesteTESTEtesteTesteTESTEtesteTesteTESTEtesteTes', 'fantasy_name': 'teste','birth_date_foundation': '10/10/1995'}, 'Entity name is not valid (OK)')

        #valids
        self.add_case_valid_size(
            {'cpf_cnpj':'14960175796','entity_name':'Teste teste', 'fantasy_name':'teste', 'birth_date_foundation':'10/10/2017'},'CPF, Name and Date are correct (OK)')
        self.add_case_valid_format(
            {'cpf_cnpj': '14960175796', 'entity_name': 'Teste teste', 'fantasy_name': 'teste',
             'birth_date_foundation': '10/10/2017'}, 'CPF, Name and Date are correct (OK)')

    def __init__(self, *args, **kwargs):
            super(RegisterEntityFormTest, self).__init__()
            unittest.TestCase.__init__(self, *args, **kwargs)
            self.set_formulary(EntityIdentificationForm)

            # test field cpf_cnpj

            # invalids
            self.add_case_invalid_format({'cpf_cnpj': None, 'entity_name': 'Teste teste', 'fantasy_name': 'teste',
                                          'birth_date_foundation': '10/10/1995'}, "CNPJ is not valid (OK)")
            self.add_case_invalid_format({'cpf_cnpj': '49518089000171', 'entity_name': None, 'fantasy_name': 'teste',
                                          'birth_date_foundation': '10/10/1995'}, "Entity name is not valid (OK)")
            self.add_case_invalid_format(
                {'cpf_cnpj': '49518089000171', 'entity_name': 'TesteMinWord', 'fantasy_name': None,
                 'birth_date_foundation': '10/10/1995'}, 'Entity Fantasy name is not valid (OK)')
            self.add_case_invalid_format(
                {'cpf_cnpj': '49518089000171', 'entity_name': 'TesteMinWord', 'fantasy_name': 'teste',
                 'birth_date_foundation': None}, 'Entity name is not valid (OK)')

            self.add_case_invalid_size({'cpf_cnpj': '', 'entity_name': 'Teste teste', 'fantasy_name': 'teste',
                                        'birth_date_foundation': '10/10/1995'}, "Cpf is not valid (OK)")
            self.add_case_invalid_size({'cpf_cnpj': '49518089000171', 'entity_name': '', 'fantasy_name': 'teste',
                                        'birth_date_foundation': '10/10/1995'}, "Entity name is not valid (OK)")
            self.add_case_invalid_size({'cpf_cnpj': '49518089000171', 'entity_name': 'TesteMinWord', 'fantasy_name': '',
                                        'birth_date_foundation': '10/10/1995'}, 'Entity Fantasy name is not valid (OK)')
            self.add_case_invalid_size(
                {'cpf_cnpj': '49518089000171', 'entity_name': 'TesteMinWord', 'fantasy_name': 'teste',
                 'birth_date_foundation': ''}, 'Entity name is not valid (OK)')
            self.add_case_invalid_size({'cpf_cnpj': '149601757961496017579614960175796', 'entity_name': 'TesteMinWord',
                                        'fantasy_name': 'teste', 'birth_date_foundation': '10/10/1995'},
                                       'Entity name is not valid (OK)')
            self.add_case_invalid_size({'cpf_cnpj': '14960175796',
                                        'entity_name': 'TESTEtesteTesteTESTEtesteTesteTESTEtesteTesteTESTEtesteTesteTESTEtesteTesteTESTEtesteTesteTESTEtesteTesteTESTEtesteTes',
                                        'fantasy_name': 'teste', 'birth_date_foundation': '10/10/1995'},
                                       'Entity name is not valid (OK)')

            # valids
            '''self.add_case_valid_size(
                {'cpf_cnpj': '49518089000171', 'entity_name': 'Teste teste', 'fantasy_name': 'teste',
                 'birth_date_foundation': '10/10/2017'}, 'CNPJ, Razao and Date are correct (OK)')
            self.add_case_valid_format(
                {'cpf_cnpj': '49518089000171', 'entity_name': 'Teste teste', 'fantasy_name': 'teste',
                 'birth_date_foundation': '10/10/2017', 'relations_company': 0, 'company_activities':0, 'market_segment':'Atacadista'}, 'CNPJ, Razao and Date are correct (OK)')'''

class RegisterFormPhone (TestAbstractForm):

    def __init__(self,*args,**kwargs):
        super(RegisterFormPhone, self).__init__()
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.set_formulary(EntityPhoneForm)

        self.add_case_valid_format({'type_contact':2,'phone':'32322525','ddd':'27', 'name':'TESTE TESTE','complemento':'TESTE'},"Valid form Contact. (OK)")

        self.add_case_invalid_format({'type_contact': 2, 'phone': None, 'ddd': '27', 'name': 'TESTE TESTE', 'complemento': 'TESTE'},"Contact phone is not valid. (OK)")
        self.add_case_invalid_format({'type_contact': 2, 'phone': '32322525', 'ddd': None, 'name': 'TESTE TESTE', 'complemento': 'TESTE'},"Contact ddd is not valid (OK)")
        self.add_case_invalid_size({'type_contact': 2, 'phone': '', 'ddd': '27', 'name': 'TESTE TESTE', 'complemento': 'TESTE'},"Contac phone is not valid. (OK)")
        self.add_case_invalid_size({'type_contact': 2, 'phone': '32322552', 'ddd': '', 'name': 'TESTE TESTE', 'complemento': 'TESTE'},"Contact dd is not valid. (OK)")
        self.add_case_invalid_size({'type_contact': 2, 'phone': '32322525', 'ddd': '27', 'name': '', 'complemento': 'TESTE'},"Contact name is not valid. (OK)")
        self.add_case_invalid_format({'type_contact': 2, 'phone': '32322525', 'ddd': '27', 'name': None, 'complemento': 'TESTE'},"Contact name is not valid. (OK)")

class RegisterFormEmail (TestAbstractForm):

    def __init__(self,*args,**kwargs):
        unittest.TestCase.__init__(self, *args,**kwargs)
        self.set_formulary(EntityEmailForm)

        self.add_case_invalid_size({'email': '','name':'TESTE','send_xml':True,'send_suitcase':False},"Email invalid email size. (OK)")
        self.add_case_invalid_size({'email': 'teste@teste.com', 'name': '', 'send_xml': True, 'send_suitcase': False},'Email invalid name size. (OK)')
        self.add_case_invalid_size({'email': 'teste@teste.com', 'name': 'TESTE', 'send_xml': '', 'send_suitcase': True},'Email invalid send_xml size. (OK)')
        self.add_case_invalid_size({'email': 'teste@teste.com', 'name': 'TESTE', 'send_xml': True, 'send_suitcase': ''},'Email invalid send_suitcase size. (OK)')
        self.add_case_invalid_format({'email': None, 'name': 'TESTE', 'send_xml': False, 'send_suitcase': True},'Email invalid email format. (OK)')
        self.add_case_invalid_format({'email': 'teste@teste.com', 'name': None, 'send_xml': False, 'send_suitcase': False},'Email invalid name format. (OK)')
        self.add_case_invalid_format({'email': 'teste@teste.com', 'name': 'TESTE', 'send_xml': None, 'send_suitcase': True},'Email invalid send_xml format. (OK)')
        self.add_case_invalid_format({'email': 'teste@teste.com', 'name': 'TESTE', 'send_xml': False, 'send_suitcase': None},'Email invalid send_suitcase format. (OK)')




