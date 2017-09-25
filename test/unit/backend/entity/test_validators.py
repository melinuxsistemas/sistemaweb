from django.test import TestCase
from modules.entity.validators import *


class ValidatorsTest(TestCase):
    def test_required_validator(self):
        case_list = [
            [None,False,"Testar validacao de campo obrigatorio com valor None. (OK)"],
            ['', False, "Testar validacao de campo obrigatorio com string vazia. (OK)"],
            ['cae', True, "Testar validacao de campo obrigatorio com numeros. (OK)"],
            ['TEXT', True, "Testar validacao de campo obrigatorio com letras. (OK)"],
            ['MORE TEXTS', True, "Testar validacao de campo obrigatorio com textos. (OK)"],
        ]
        self.execute_case_list(case_list, required_validator)

    def test_min_words_name_validator(self):
        case_list = [
            [None,False,"Testar validacao de numero minimo de palavras com valor None. (OK)"],
            ['',False,"Testar validacao de numero minimo de palavras com string vazia. (OK)"],
            ['TESTE', False, "Testar validacao de numero minimo de palavras com uma palavra. (OK)"],
            ['TESTE ', False, "Testar validacao de numero minimo de palavras com uma palavra e um espaco vazio. (OK)"],
            ['TESTE TESTE', True, "Testar validacao de numero minimo de palavras com duas palavras. (OK)"]
        ]
        self.execute_case_list(case_list, min_words_name_validator)



    def execute_case_list(self,case_list, validator):
        for value, expected_result, description in case_list:
            print("VEJA OS VALORES: ",value, expected_result, description)
            try:
                result = validator(value)
            except:
                result = False
            self.assertEqual(result, expected_result, description)

