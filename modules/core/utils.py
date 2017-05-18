from django.core import serializers
from django.core.mail import EmailMessage
from django.http import HttpResponse

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

def enviaemail(email):
   html_content = "<strong>CONFIRMAÇÃO DE REGISTRO</strong><br>" \
                  "<p>Para ter acesso ao Sistema clique no link e informe" \
                  "o numero de registro abcbd12345789</>"
   email = EmailMessage("Confirmação de registro", html_content, "melinuxsistemas@gmail.com", [ email])
   email.content_subtype = "html"
   res = email.send()
   return
