from django.core import serializers
from django.core.mail import EmailMessage
from conf.vars.messages.email import reset_email
from modules.usuario.validators import check_email_format
import hashlib
import threading
import datetime


def response_format_success(object,list_fields):
    return response_format(True, '', object, list_fields)

def response_format_error(message):
    return response_format(False, message, None, None)

def response_format(result,message,object,list_fields):
    response_dict = {}
    response_dict['success'] = result
    response_dict['message'] = message
    if result:
        response_dict['data-object'] = serializers.serialize('json', [object], fields=tuple(list_fields))
        response_dict['data-object'] = response_dict['data-object'][1:-1]

    else:
        response_dict['data-object'] = None
    return response_dict


"""
def executar_operacao(registro,operacao):
    response_dict = {}
    if operacao == "save":
        metodo_selecionado = registro.save
        menssage_sucesso = "Registro adicionado com Sucesso!"
        menssage_falha = "Erro! Falha na inclusão do registro (\n"

    elif operacao == "delete":
        metodo_selecionado = registro.delete
        menssage_sucesso = "Registro apagado com Sucesso!"
        menssage_falha = "Erro! Falha na exclusão do registro (\n"

    try:
        metodo_selecionado();
        response_dict['success'] = True
        response_dict['message'] = menssage_sucesso
        response_dict['data-object'] = serialize('json',registro)

    except Exception as e:
        response_dict['success'] = False
        response_dict['message'] = menssage_falha+str(e)+")."
        response_dict['data-object'] = None
    return response_dict
"""


def send_email(to_address, title, message):
    from_address = 'melinuxsistemas@gmail.com'
    email = EmailMessage(title, message, from_address, [to_address])
    email.content_subtype = "html"
    if check_email_format(from_address):
        try:
            thread = threading.Thread(name='send_email', target=email.send)
            thread.start()
            return True

        except Exception as e:
            return False
    else:
        return False


def generate_activation_code(email):
    if email is not None:
        data_reg = datetime.datetime.now()
        ano_reg = str(data_reg.year)[::-1]
        mes_reg = str(data_reg.month)[::-1] if data_reg.month >= 10 else str(data_reg.month*10)
        dia_reg = str(data_reg.day)[::-1] if data_reg.day >= 10 else str(data_reg.day*10)
        hora_reg = str(data_reg.hour)[::-1] if data_reg.hour >= 10 else str(data_reg.hour * 10)
        min_reg  = str(data_reg.minute)[::-1] if data_reg.minute >= 10 else str(data_reg.minute * 10)
        seg_reg  = str(data_reg.second)[::-1] if data_reg.second >= 10 else str(data_reg.second * 10)
        email_md5 = encode_hash_email(email)
        hash_final = str(email_md5[0:5] + ano_reg + email_md5[5:5 + 5] + mes_reg + email_md5[10:10 + 5] + dia_reg
                         + email_md5[15:15 + 5] + seg_reg + email_md5[20:20 + 5] + min_reg + email_md5[25:25 + 5]
                         + hora_reg + email_md5[30:])
        return hash_final
    else:
        return None


def decode_activation_code(activation_code):
    if len(activation_code) == 46:
        year = str(activation_code[5:5 + 4])
        month = str(activation_code[14:14 + 2])
        day = str(activation_code[21:21 + 2])
        hours = str(activation_code[42:42 + 2])
        minutes = str(activation_code[35:35 + 2])
        seconds = str(activation_code[28:28 + 2])
        hash_email = str(activation_code[:5] + activation_code[9:9 + 5] + activation_code[16:16 + 5] + activation_code[23:23 + 5] + activation_code[30:30 + 5] + activation_code[37:37 + 5] + activation_code[44:])
        date = datetime.datetime(int(year[::-1]),int(month[::-1]),int(day[::-1]),int(hours[::-1]),int(minutes[::-1]),int(seconds[::-1]))
        return hash_email, date
    else:
        return None, None


def encode_hash_email(email):
    hash_email = hashlib.md5()
    hash_email.update(email.encode('utf-8'))
    return hash_email.hexdigest()


def check_valid_activation_code(email,activation_code):
    from modules.usuario.models import Usuario
    email_code, date_code = decode_activation_code(activation_code)
    if email_code is not None and date_code is not None:
        hash_email_test = encode_hash_email(email)
        current_date = datetime.datetime.now()
        email_code_is_valid = email_code == hash_email_test
        activation_code_is_unique = Usuario.objects.activation_code_is_unique(activation_code)
        date_code_is_expired = date_code > (current_date + datetime.timedelta(1))

        if email_code_is_valid and activation_code_is_unique and not date_code_is_expired:
            return True
        else:
            return False
    else:
        return False

def generate_random_password(email):
    nova_senha = encode_hash_email(str(email) + str(datetime.datetime.now()))[15:15 + 8]
    return nova_senha


def send_generate_activation_code(email,activation_code):
    html_content = reset_email
    #"<strong>Cadastro realizado com Sucesso!</strong><br>" \
    #"<p>Para começar <a href='http://localhost:8000/register/activate/"+email+"/"+activation_code+"/'"+">Clique aqui</a></p>"
    return send_email(to_address=email, title="Melinux Sistema - Confirmação de email", message=html_content)


def send_reset_password(senha, email):
    html_content = reset_email
    #print("VEJA O EMAIL QUE VAI PRO CARA: ",html_content)
    #<strong>Senha de acesso redefinida com Sucesso!</strong><br>" \
    #              "<p>Uma nova senha provisória foi gerada para permitir o acesso à sua conta.<br>" \
    #              "A troca por uma senha de sua preferência é altamente recomendado, para isso acesse a pàgina do seu perfil.</p>" \
    #              "<br><p>Senha de Acesso:"+senha+"</p><br>"
    #
    return send_email(to_address=email,title="Melinux Sistema - Recuperar senha de Acesso", message=html_content)