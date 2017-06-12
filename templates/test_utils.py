from django.test import TestCase
from modules.core import utils

class ActivationTests(TestCase):

    def test_gera_chave(self):
        lista_opcoes = [
            ['123456',False],
            ['', False],
            ['abcdefghijk', False],
            ['1q2we45tfg76789bggg', False],
            [None, False],
            ['teste@teste.com', True],

        ]
        for item in lista_opcoes:
            chave = utils.gera_chave(item[0])
            self.assertEqual(len(chave) == 46,True,"Testar Validacao do tamanho da chave (OK)")

    def test_valida_chave(self):
        lista_chave = [
            ['abcdfefrghukjkkkkkkk',False],
            ['1234566gv67hhhh89yy456rt79895',False],
            ['', False],
            ['476377102576206035580602d7ae44c47d894f0153418c', False],
            ['476377102576206035280602d7ae75c47d894f0153416c',True],
        ]
        for item in lista_chave:
            data, chave = utils.valida_chave(item[0])
            dta_ok, chave_ok = utils.valida_chave('476377102576206035280602d7ae75c47d894f0153416c')
            self.assertEqual((data == dta_ok and chave == chave_ok), item[1],"Teste de validação de chave (OK)")