import os
from bs4 import BeautifulSoup


class BaseTypeEmail:

    data_paramters = {}
    data_paramters['COMPANY_NAME'] = "MelinuxWeb - Soluções em Tecnologias e Consultorias LTDA"
    data_paramters['COMPANY_ADDRESS_STREET'] = "Rua Demósthenes Nunes Vieira, 60, Alto Lage"
    data_paramters['COMPANY_ADDRESS_CITY'] = "Caríacica, Espírito Santo, Brasil - 29.151-260"
    data_paramters['COMPANY_SITE'] = "www.melinuxsistemas.com.br"
    data_paramters['COMPANY_COMERCIAL_NUMBER'] = "(27) 99988-1254"
    data_paramters['COMPANY_SUPORT_NUMBER'] = "(27) 3043-0703"
    data_paramters['COMPANY_USER_NAME'] = "Equipe Melinux"

    title = None
    message = None


    def ConvertTemplate(self,template):
        path = os.path.abspath(__file__).replace("email.py", "/templates/" + template)
        with open(path, 'rt', encoding='utf-8') as file:
            html_file = str(BeautifulSoup(file, "html.parser").find('body'))
            for item in self.data_paramters:
                html_file = html_file.replace("{{ "+item+" }}",self.data_paramters[item])
            return html_file
        return None


class ConfirmationsTypeEmail(BaseTypeEmail):

    def __init__(self):
        self.confirmation_user_email = self.ConvertTemplate('confirm_email.html')
        self.resend_activation_code_email = self.ConvertTemplate('resend_activation_code_email.html')
        self.reset_password_email = self.ConvertTemplate('reset_password_email.html')


