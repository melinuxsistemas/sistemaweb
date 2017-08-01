from unittest import TestCase
import unittest

from modules.entity.forms import FormPersonEntity, FormCompanyEntity
from test.unit.backend.core.test_forms import TestAbstractForm


class RegisterEntityFormTest (TestAbstractForm):

    def __init__(self,*args, **kwargs):
        super(RegisterEntityFormTest, self).__init__()
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.set_formulary(FormPersonEntity)

        #test field cpf_cnpj

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
            self.set_formulary(FormCompanyEntity)

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