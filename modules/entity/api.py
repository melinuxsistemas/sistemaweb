from django.contrib.auth.decorators import login_required

from modules.core.api import AbstractAPI
from modules.core.config import ERRORS_MESSAGES
from modules.core.utils import response_format_success, response_format_error, generate_activation_code, json_serial
from modules.core.comunications import send_generate_activation_code
from modules.entity.forms import FormCompanyEntity, FormPersonEntity, FormRegisterPhone, FormRegisterEmailEntity
from modules.entity.models import Entity, Contact, Email
from modules.user.models import User
from django.http import HttpResponse
from django.http import Http404
from sistemaweb import settings
import json


def cria_dict(type_object, item):
    if (type_object == 'Email'):
        if item.send_xml:
            xml = 'Sim'
        else:
            xml = 'Não'
        if item.send_suitcase:
            suitcase = 'Sim'
        else:
            suitcase = 'Não'
        return {'id':item.id,'name': item.name, 'email': item.email, 'send_xml': xml, 'send_suitcase': suitcase}
    if (type_object == 'Contact'):
        return {'id': item.id, 'type_contact': item.type_contact, 'phone': '(' + item.ddd + ')' + item.phone,
                'complemento': item.complemento, 'name': item.name}
    if (type_object == 'Entity'):
        if item.birth_date_foundation is not None:
            date = item.birth_date_foundation.strftime('%d/%m/%Y')
        else:
            date = None
        return {'id': item.id, 'birth_date_foundation': date, 'entity_type' : item.entity_type,
            'cpf_cnpj' : item.cpf_cnpj, 'entity_name' : item.entity_name,'created_date' : item.created_date.strftime('%d/%m/%Y'),
        'selected' : ''}

def format_exception_message(exceptions):
    message_dict = {}
    if type(exceptions) == list:
        #print("VEJAMOS O QUE TEMOS: ",exceptions)
        for item in exceptions:
            #print("VEJA OS ARGUMENTOS: ",item.args)
            if len(item.args) > 1:
                status_code = item.args[1]
                except_parts = str(item).replace("['", "").replace("']", "")
                if ": " in except_parts:
                    except_parts = except_parts.split(': ')
                    field = except_parts[0]

                else:
                    field = "Erro! Formato de mensagem nao foi gerado pois o campo do formulario e desconhecido."
            else:
                if 'UNIQUE' in item.args[0]:
                    status_code = 'unique'

                except_parts = str(item)
                if ": " in except_parts:
                    except_parts = except_parts.split(': ')
                    field = except_parts[1].split('.')[1]

            """ 
            Quando temos apenas um erro esse e o formato da excessao:
               django.core.exceptions.ValidationError: ['cpf_cnpj: Cpf number is not valid.']
            
            Contudo pode ser que o mesmo campo tenha duas validacoes com erro 
            sendo necessario adequar essa funcao para tratar isso.
            """
            message_dict[field] = ERRORS_MESSAGES[status_code]

    else:
        print("VEJA O QUE TEMOS: ", exceptions, type(exceptions))
        paramters = exceptions.args[0].split(': ')
        code_status = exceptions.args[1]
        field = paramters[0]
        #value = paramters[1]
        message_dict[field] = ERRORS_MESSAGES[code_status]
    return message_dict


class EntityAPI:

    @login_required
    def save_person(request):
        print("Vindo aqui save_person")
        resultado, form = AbstractAPI.filter_request(request, FormPersonEntity)
        entity = Entity()
        entity.form_to_object(form)
        response_dict = {}
        if resultado:
            try:
                entity.save()
                response_dict = response_format_success(entity, ['id','cpf_cnpj','entity_name','entity_type','birth_date_foundation','created_date'])
                #entity.show_fields_value()
            except Exception as e:
                print("VEJA A EXCECAO QUE DEU: ",e)
                response_dict = response_format_error(format_exception_message(entity.model_exceptions))

        else:
            entity.check_validators()
            model_exceptions = format_exception_message(entity.model_exceptions)
            form_exceptions = form.format_validate_response()

            full_exceptions = {}#dict(form_exceptions, **model_exceptions);
            full_exceptions.update(model_exceptions)
            full_exceptions.update(form_exceptions)

            #print("RESPONSE FORM EXCEPTIONS: ", form_exceptions)
            #print("RESPONSE MODEL EXCEPTIONS: ", model_exceptions)
            #print("RESPONSE FULL EXCEPTIONS: ", full_exceptions)
            response_dict = response_format_error(full_exceptions)

        #print("RESPONSE_DICT: ",response_dict)
        return HttpResponse(json.dumps(response_dict))

    '''def save_email (request,id_entity):
        #Falta deixar padronizado criando save da class Email

        resultado , form = AbstractAPI.filter_request(request,FormRegisterEmailEntity)

        if resultado:
            email = Email()
            email.entity_id = 1
            email.form_to_object(form)
            email.send_xml = request.POST['send_xml']
            email.send_suitcase = request.POST['send_suitcase']
            email.show_fields_value()

        try:
            email.save()
            response_dict = response_format_success(email,['entity','name','email','send_xml','send_suitcase'])
        except:
            print("Nao salvei")
            response_dict = response_format_error(False)
        return HttpResponse(json.dumps(response_dict))

        def save_number(request, id_entity):
        list = {"Email": Email, "Entity": Entity}
        test = list["Email"]()
        test.show_fields_value()
        resultado, form = AbstractAPI.filter_request(request, FormRegisterPhone)
        resultado = True
        contact = Contact()
        contact.entity_id = id_entity
        contact.form_to_object(form)
        contact.show_fields_value()
        if resultado:
            try:
                contact.save()
                response_dict = response_format_success(contact,['entity','name','type_contact','ddd','phone','complemento'])
                print("Saindo do save number")
                #contact.show_fields_value()
            except Exception as e:
                print("Veja o q acontece",e)
                response_dict = response_format_error(format_exception_message(contact.model_exceptions))
                print("O resultado da Exception é:  ",response_dict)
        else:
            contact.check_validators()
            model_exceptions = format_exception_message(contact.model_exceptions)
            form_exceptions = form.format_validate_response()

            full_exceptions = {}  # dict(form_exceptions, **model_exceptions);
            full_exceptions.update(model_exceptions)
            full_exceptions.update(form_exceptions)
            response_dict = response_format_error(full_exceptions)
        print("RESPONSE DICT",response_dict)
        return HttpResponse(json.dumps(response_dict))'''

    #SAVE GENÉRICO
    def save_genérico (request,id_entity):
        #No request eu terei q passar o Form e a Classe
        type_object = request.POST['type_class']
        list_class = {"Email": Email, "Contact": Contact}
        list_forms = {"Email": FormRegisterEmailEntity, "Contact": FormRegisterPhone }
        object = list_class[type_object]()
        form_object = list_forms[type_object]

        #object.show_fields_value()
        print("Olha o form",form_object)
        result , form = AbstractAPI.filter_request(request,form_object)
        result = True
        if result:
            object.entity_id = id_entity
            object.form_to_object(form)
            object.show_fields_value()
            try:
                object.save()
                #falta fazer lista de campos dinamica
                response_dict = response_format_success(object,['entity', 'name', 'type_contact', 'ddd', 'phone', 'complemento'])
                print("Saindo do save")
            except Exception as e:
                print("Veja o q acontece", e)
                response_dict = response_format_error(format_exception_message(object.model_exceptions))
                print("O resultado da Exception é:  ", response_dict)
        else:
            object.check_validators()
            model_exceptions = format_exception_message(object.model_exceptions)
            form_exceptions = form.format_validate_response()

            full_exceptions = {}  # dict(form_exceptions, **model_exceptions);
            full_exceptions.update(model_exceptions)
            full_exceptions.update(form_exceptions)
            response_dict = response_format_error(full_exceptions)

        return HttpResponse(json.dumps(response_dict))

    #LOAD TABELA GENÉRICO
    def load_generico (request,id_entity,type_class):
        # No request eu terei q passar o Form e a Classe
        type_object = type_class
        list_class = {"Email": Email, "Contact": Contact, "Entity": Entity}
        object = list_class[type_object]
        if id_entity != 'entity':
            list_objects = object.objects.filter(entity_id=id_entity)
        else:
            list_objects = object.objects.all().order_by('-id')

        response_dict = []
        for item in list_objects:
            dict = cria_dict(type_object,item)
            response_dict.append(dict)

        return HttpResponse(json.dumps(response_dict))

    #DELETE GENÉRICO
    def delete_generico (request,id,type_class):
        list_class = {"Email": Email, "Contact": Contact, "Entity": Entity}
        type_object = list_class[type_class]
        object = type_object.objects.get(id=id)
        try:
            object.desativar()
        except:
            pass
        return HttpResponse(json.dumps({}))



    #Deleta um contato
    def delete_contact (request, id_contact):
        print("Ja vindo aqui",id_contact)
        contact = Contact.objects.filter(id=id_contact)
        try:
            contact.delete()
            print("JA EXCLUI")
        except:
            print("DANDO ERROR")
        response_dict = []
        return HttpResponse(json.dumps(response_dict))

    #Carrega os dados de um Contato para o Modal
    def load_field_contact (request, id_contact):
        response_contact = {}
        print (id_contact)
        try:
            contact = Contact.objects.get(id=id_contact)
            response_contact['type_contact'] = contact.type_contact
            response_contact['phone'] = contact.phone
            response_contact['name'] = contact.name
            response_contact['ddd'] = contact.ddd
            response_contact['complemento'] = contact.complemento
        except:
            response_contact = response_format_error(False)
        print("OLHA O Q EU VOU RETORNAR: response_contact", response_contact)
        return HttpResponse(json.dumps(response_contact))

    #Atualiza os dados de um Contato
    def update_contact (request):

        id_contact = request.POST['id']
        phone = request.POST['phone']
        name = request.POST['name']
        ddd = request.POST['ddd']
        type_contact = request.POST['type_contact']
        complemento = request.POST['complemento']
        contact = Contact.objects.get(id=id_contact)
        contact.show_fields_value()

        try:
            Contact.objects.filter(id=id_contact).update(phone= phone, name=name,ddd=ddd,type_contact=type_contact,complemento=complemento)
            response_dict = response_format_success(contact,['phone','name','ddd','type_contact','complemento'])
        except:
            response_dict = response_format_error(False)
        return  HttpResponse(json.dumps(response_dict))

    def update_email (request):
        id_email = request.POST['id']
        email = request.POST['email']
        name = request.POST['name']
        send_xml = request.POST['send_xml']
        send_suitcase = request.POST['send_suitcase']
        email_object = Email.objects.get(id=id_email)
        email_object.show_fields_value()

        try:
            Email.objects.filter(id=id_email).update(email=email, name=name, send_xml=send_xml, send_suitcase=send_suitcase)
            response_dict = response_format_success(email_object,['email', 'name', 'send_xml', 'send_suitcase'])
        except:
            response_dict = response_format_error(False)
        return HttpResponse(json.dumps(response_dict))

    """
    def register_delete(request, email):
        user = User.objects.get_user_email(email)
        if user is not None:
            user.delete()
            response_dict = response_format_error("Usuario deletado com sucesso.")
        else:
            response_dict = response_format_error("Usuario nao existe.")
        return HttpResponse(json.dumps(response_dict))

    def generate_new_activation_code(request):
        resultado, form = AbstractAPI.filter_request(request, FormResetPassword)
        if resultado:
            email = request.POST['email'].lower()
            usuario = User.objects.get_user_email(email)
            if usuario is not None:
                if not usuario.account_activated:
                    activation_code = generate_activation_code(email)
                    resend_generate_activation_code(email, activation_code)
                    response_dict = response_format_success(usuario, ['email'])
                else:
                    response_dict = response_format_error("Essa conta já foi ativada.")
            else:
                response_dict = response_format_error("Email não cadastrado.")
        else:
            response_dict = response_format_error("Email com formato inválido.")
        return HttpResponse(json.dumps(response_dict))

    def activate_account(request):
        result, form = AbstractAPI.filter_request(request)
        if result:
            usuario = User.objects.activate_account(True)
            response_dict = response_format_success(usuario, ['account_activated'])
        return HttpResponse(json.dumps(response_dict))

    def login_autentication(request):
        resultado, form = AbstractAPI.filter_request(request, FormLogin)
        if resultado:
            email = request.POST['email'].lower()
            password = request.POST['password']
            user = User.objects.get_user_email(email=email)
            if user is not None:
                if user.account_activated:
                    if user.is_active:
                        auth = User.objects.authenticate(request, email=email, password=password)
                        if auth is not None:
                            login(request, user)
                            response_dict = response_format_success(user, ['email'])
                        else:
                            response_dict = response_format_error("Usuário ou senha incorreta.")
                    else:
                        response_dict = response_format_error("Usuário não autorizado.")
                else:
                    response_dict = response_format_error("Usuário não confirmado.")
            else:
                response_dict = response_format_error("Usuário não existe.")
        else:
            response_dict = response_format_error("Formulário com dados inválidos.")
        return HttpResponse(json.dumps(response_dict))

    def reset_password(request):
        resultado, form = AbstractAPI.filter_request(request, FormResetPassword)
        if resultado:
            email = request.POST['email'].lower()
            usuario = User.objects.get_user_email(email)
            if usuario is not None:
                try:
                    nova_senha = generate_random_password(email)
                    usuario.set_password(nova_senha)
                    usuario.save()
                    send_reset_password(nova_senha, email)
                    response_dict = response_format_success(usuario, ['email'])
                except:
                    response_dict = response_format_success(usuario, ['email'])
            else:
                response_dict = response_format_error("Email não cadastrado.")
        else:
            response_dict = response_format_error("Formulário com dados inválidos.")
        return HttpResponse(json.dumps(response_dict))

    def change_password(request):
        result, form = AbstractAPI.filter_request(request, FormChangePassword)
        if result:
            usuario = request.user
            if usuario.check_password(form.cleaned_data['old_password']):
                usuario.change_password(form.cleaned_data['password'])
                auth = User.objects.authenticate(request, email=usuario.email, password=usuario.password)
                auth_user = User.objects.get_user_email(usuario.email)
                if auth is not None and usuario.is_active:
                    #login(request, auth_user)
                    pass
                else:
                    response_dict = response_format_error("Não foi possivel autenticar seu usuário<br>com a senha redefinida.")

                response_dict = response_format_success(request.user,"Usuário alterado com sucesso.")
            else:
                response_dict = response_format_error("Erro! Senha antiga está incorreta.")
        else:
            response_dict = response_format_error(form.format_validate_response())

        return HttpResponse(json.dumps(response_dict))
    """

