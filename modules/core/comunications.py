from conf.configuration import SystemVariables
from modules.core.utils import send_email


def send_generate_activation_code(email,activation_code):
    html_content = SystemVariables.messages_email.confirmation_user_email
    url_confirmation = "http://localhost:8000/register/activate/"+email+"/"+activation_code+"/"
    html_content = html_content.replace('{{ CONFIRMATION_URL }}',url_confirmation)
    return send_email(to_address=email, title="Melinux Sistema - Confirmação de email", message=html_content)


def resend_generate_activation_code(email,activation_code):
    html_content = SystemVariables.messages_email.resend_activation_code_email
    url_confirmation = "http://localhost:8000/register/activate/"+email+"/"+activation_code+"/"
    html_content = html_content.replace('{{ CONFIRMATION_URL }}',url_confirmation)
    return send_email(to_address=email, title="Melinux Sistema - Confirmação de email", message=html_content)


def send_reset_password(senha, email):
    html_content = ""#confirmation_personal_email
    #print("VEJA O EMAIL QUE VAI PRO CARA: ",html_content)
    #<strong>Senha de acesso redefinida com Sucesso!</strong><br>" \
    #              "<p>Uma nova senha provisória foi gerada para permitir o acesso à sua conta.<br>" \
    #              "A troca por uma senha de sua preferência é altamente recomendado, para isso acesse a pàgina do seu perfil.</p>" \
    #              "<br><p>Senha de Acesso:"+senha+"</p><br>"
    #
    return send_email(to_address=email,title="Melinux Sistema - Recuperar senha de Acesso", message=html_content)