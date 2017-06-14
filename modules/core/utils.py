from django.core import serializers
from django.core.mail import EmailMessage
import hashlib
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


def envia_email(email):
   chave = create_activation_code(email)
   html_content = "<strong>CONFIRMAÇÃO DE REGISTRO</strong><br>" \
                  "<p>Para ter acesso ao Sistema acesse o link abaixo e informe " \
                  "o numero de registro :</p><br><a href='http://localhost:8000/activate/"+email+"/"+chave+"/'"+">Clique aqui</a>"
   email = EmailMessage("Confirmação de registro", html_content, "melinuxsistemas@gmail.com", [ email])
   email.content_subtype = "html"
   result = email.send()
   return result

def create_activation_code(email):

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


def decode_activation_code(activation_code):
    year = str(activation_code[5:5 + 4])
    month = str(activation_code[14:14 + 2])
    day = str(activation_code[21:21 + 2])
    hours = str(activation_code[42:42 + 2])
    minutes = str(activation_code[35:35 + 2])
    seconds = str(activation_code[28:28 + 2])
    hash_email = str(activation_code[:5] + activation_code[9:9 + 5] + activation_code[16:16 + 5] + activation_code[23:23 + 5] + activation_code[30:30 + 5] + activation_code[37:37 + 5] + activation_code[44:])
    date = datetime.datetime(int(year[::-1]),int(month[::-1]),int(day[::-1]),int(hours[::-1]),int(minutes[::-1]),int(seconds[::-1]))
    return hash_email, date


def encode_hash_email(email):
    hash_email = hashlib.md5()
    hash_email.update(email.encode('utf-8'))
    return hash_email.hexdigest()


def generate_random_password(email):
    nova_senha = encode_hash_email(str(email) + str(datetime.datetime.now()))[15:15 + 8]
    send_reset_password(nova_senha, email)
    return nova_senha


def send_reset_password(senha, email):
   html_content = "<strong>NOVA SENHA GERADA COM SUCESSO</strong><br>" \
                  "<p>Uma nova senha provisória foi gerada para acessar o Sistema, após o login " \
                  "acesse seu perfil e troque sua senha .</p><br><p>Sua nova senha :"+senha+"</p><br>"
   email = EmailMessage("Solicitação de nova senha", html_content, "melinuxsistemas@gmail.com", [email])
   email.content_subtype = "html"
   result = email.send()
   return result
