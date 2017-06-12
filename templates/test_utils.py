from django.test import TestCase
import json

"""
Desenvolver mecanismo para certificar o envio dos emails.
class EmailTest(TestCase):

    def test_emtpy_validator(self):
        self.assertEqual(is_empty(""), True, "Testar Validacao de valor vazio para campo vazio (OK)")
        self.assertEqual(is_empty("teste"), False, "Testar Validacao de valor vazio para campo preenchido (OK)")

    def test_send_email(self):
        # Envia mensagem.
        mail.send_mail('Assunto aqui', 'Aqui vai a mensagem.',
            'from@example.com', ['to@example.com'],
            fail_silently=False)

        # Verifica se uma mensagem foi enviada.
        self.assertEqual(len(mail.outbox), 1)

        # Verifica se o assunto da mensagem é igual
        self.assertEqual(mail.outbox[0].subject, 'Assunto aqui')

"""

class ActivationCodeTest(TestCase):

    def test_create_hash_email(self):
        #self.assertEqual(is_empty(""), True, "Testar Validacao de valor vazio para campo vazio (OK)")
        #self.assertEqual(is_empty("teste"), False, "Testar Validacao de valor vazio para campo preenchido (OK)")
        pass

    def test_create_activation_code(self):
        pass


