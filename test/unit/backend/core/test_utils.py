from django.core.mail import mail
from django.test import TestCase


class EmailTest(TestCase):
    def test_send_email(self):
        # Envia mensagem.
        mail.send_mail('Assunto aqui', 'Aqui vai a mensagem.',
            'from@example.com', ['to@example.com'],
            fail_silently=False)

        # Verifica se uma mensagem foi enviada.
        self.assertEqual(len(mail.outbox), 1)

        # Verifica se o assunto da mensagem é igual
        self.assertEqual(mail.outbox[0].subject, 'Assunto aqui')
