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
        print("Campos",list_fields)
        response_dict['data-object'] = serializers.serialize('json', [object], list_fields)
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
   chave = gera_chave(email)

   html_content = "<strong>CONFIRMAÇÃO DE REGISTRO</strong><br>" \
                  "<p>Para ter acesso ao Sistema acesse o link abaixo e informe " \
                  "o numero de registro :</p><br><a href='http://localhost:8000/activate/"+email+"/"+chave+"/'"+">Clique aqui</a>"
   email = EmailMessage("Confirmação de registro", html_content, "melinuxsistemas@gmail.com", [ email])
   email.content_subtype = "html"
   result = email.send()
   return result

def gera_chave(email):
    data_reg = datetime.datetime.now()
    ano_reg = str(data_reg.year)[::-1]
    mes_reg = str(data_reg.month)[::-1] if data_reg.month >= 10 else str(data_reg.month*10)
    dia_reg = str(data_reg.day)[::-1] if data_reg.day >= 10 else str(data_reg.day*10)
    hora_reg = str(data_reg.hour)[::-1] if data_reg.hour >= 10 else str(data_reg.hour * 10)
    min_reg  = str(data_reg.minute)[::-1] if data_reg.minute >= 10 else str(data_reg.minute * 10)
    seg_reg  = str(data_reg.second)[::-1] if data_reg.second >= 10 else str(data_reg.second * 10)

    email_md5 = gera_hash_md5(email)

    hash_final = str(email_md5[0:5] + ano_reg + email_md5[5:5 + 5] + mes_reg + email_md5[10:10 + 5] + dia_reg
                     + email_md5[15:15 + 5] + seg_reg + email_md5[20:20 + 5] + min_reg + email_md5[25:25 + 5]
                     + hora_reg + email_md5[30:])
    return hash_final

def gera_hash_md5(email):

    hash_email = hashlib.md5()
    hash_email.update(email.encode('utf-8'))

    return hash_email.hexdigest()

def valida_chave(chave):

    ano = str(chave[5:5 +4])
    mes = str(chave[14:14 +2])
    dia = str(chave[21:21 +2])
    hora = str(chave[42:42 +2])
    minutos = str(chave[35:35 +2])
    segundos = str(chave[28:28 +2])

    chave = str(chave[:5]+chave[9:9 +5]+chave[16:16 +5]+chave[23:23 +5]+chave[30:30 +5]+chave[37:37 +5]+chave[44:])
    data = datetime.datetime(int(ano[::-1]),int(mes[::-1]),int(dia[::-1]),int(hora[::-1]),int(minutos[::-1]),int(segundos[::-1]))

    return chave, data