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

    def test_minimum_age_person_validator(self):
        case_list = [
            [None, True, "Testar validacao da idade minima com valor None. (OK)"],
            ['', True, "Testar validacao de idade minima com string vazia. (OK)"],
            [' ', False, "Testar validacao de idade minima com texto contendo um espaço em branco. (OK)"],
            ['TESTE', False, "Testar validacao de idade minima com uma palavra. (OK)"],
            ['20', True, "Testar validacao de idade minima usando uma string contendo numeros. (OK)"],
            #[15, False, "Testar validacao de idade minima com um numero menor que o minimo. (OK)"],
            #[18, True, "Testar validacao de idade minima com um numero igual ao minimo. (OK)"],
            #[25, True, "Testar validacao de idade minima com um numero maior que o minimo. (OK)"]
        ]
        self.execute_case_list(case_list, minimum_age_person_validator)

    def execute_case_list(self,case_list, validator):
        for value, expected_result, description in case_list:
            print("VEJA OS VALORES: ", value, expected_result, description)
            if validator == minimum_age_person_validator:
                if type(value) == int:
                    value = value.date()
                    current_date = datetime.datetime.now().date()
                    time_diff = ((current_date - value).days) / 365.25
                    print("VEJA A DIFERENCA PRO ANO ATUAL: ", time_diff)


            try:
                result = validator(value)
            except:
                result = False
            self.assertEqual(result, expected_result, description)

    def test_only_numeric_phone_validator(self):
        case_list = [
            [None,False,"Testar validação do telefone com valor None. (OK)"],
            ['',False,"Testar validação do telefone com string vazia. (OK)"],
            [' ',False,'Testar validação do telefone com texto contendo espaço vazio. (OK)'],
            ['TESTE123',False,'Testar validação do telefone com valor contento letras. (OK)'],
            ['30304050',True,'Testar validação do telefone com string contendo somente numeros. (OK)']
        ]
        self.execute_case_list(case_list, only_numeric)



