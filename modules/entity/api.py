from modules.core.api import AbstractAPI
from modules.core.config import ERRORS_MESSAGES
from modules.core.utils import response_format_success, response_format_error, generate_activation_code
from modules.core.comunications import send_generate_activation_code
from modules.entity.forms import FormCompanyEntity, FormPersonEntity, FormRegisterPhone
from modules.entity.models import Entity, Contact
from modules.user.models import User
from django.http import HttpResponse
from django.http import Http404
from sistemaweb import settings
import json


def format_exception_message(exceptions):
    message_dict = {}
    if type(exceptions) == list:
        print("VEJAMOS O QUE TEMOS: ",exceptions)
        for item in exceptions:
            print("VEJA OS ARGUMENTOS: ",item.args)
            if len(item.args) > 1:
                status_code = item.args[1]
                except_parts = str(item).replace("['", "").replace("']", "")
                if ": " in except_parts:
                    except_parts = except_parts.split(': ')
                    field = except_parts[0]

                else:
                    field = "QUEM SERA?"
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

    def save_person(request):
        resultado, form = AbstractAPI.filter_request(request, FormPersonEntity)
        entity = Entity()
        entity.form_to_object(form)
        response_dict = {}
        if resultado:
            try:
                entity.save()
                response_dict = response_format_success(entity, ['cpf_cnpj','entity_name','fantasy_name','birth_date_foundation'])
                entity.show_fields_value()
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

        print("RESPONSE_DICT: ",response_dict)
        return HttpResponse(json.dumps(response_dict))

    def save_number(request):
        resultado, form = AbstractAPI.filter_request(request, FormRegisterPhone)
        print("Olha o Resultado do save",resultado)
        contact = Contact()
        contact.entity_id = 1
        contact.form_to_object(form)
        contact.show_fields_value()
        try:
            contact.save()
            print("Entrando para salvar")
            response_dict = response_format_success(contact,['entity','name','type_contact','ddd','phone','operadora'])
            #contact.show_fields_value()
        except:
            response_dict = response_format_error(False)
        return HttpResponse(json.dumps(response_dict))

    def load_contacts(request, cpf_cnpj):
        print("To vindo aqui? \n")
        print("Olha o cfp:",cpf_cnpj)
        contacts = Contact.objects.filter(entity_id=1)

        response_dict = []
        for item in contacts:
            print('Olha o item',item.type_contact)
            response_contacts = {}
            response_contacts['type_contact'] = item.type_contact
            response_contacts['phone'] = '(' + item.ddd + ')' + item.phone
            response_contacts['operadora'] = item.operadora
            response_contacts['name'] = item.name
            response_dict.append(response_contacts)
        print(response_dict)
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

