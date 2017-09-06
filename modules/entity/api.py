from modules.core.api import AbstractAPI
from modules.core.config import ERRORS_MESSAGES
from modules.core.utils import response_format_success, response_format_error, generate_activation_code
from modules.core.comunications import send_generate_activation_code
from modules.entity.forms import FormCompanyEntity,FormPersonEntity
from modules.entity.models import Entity
from modules.user.models import User
from django.http import HttpResponse
from django.http import Http404
from sistemaweb import settings
import json



class EntityAPI:

    def save_person(request):
        resultado, form = AbstractAPI.filter_request(request, FormPersonEntity)
        if resultado:
            entity = Entity()
            entity.form_to_object(form)

            try:
                entity.save()
                response_dict = response_format_success(entity, ['cpf_cnpj','entity_name','fantasy_name','birth_date_foundation'])
                entity.show_fields_value()
            except Exception as e:
                message_dict = {}
                for erro in e.args:
                    list_fields = erro.split(":")
                    field = list_fields[1].split('.')[1]
                    value = list_fields[0]
                    for item in ERRORS_MESSAGES:
                        if item in list_fields[0].lower():
                            value = ERRORS_MESSAGES[item]
                    message_dict[field] = value
                response_dict = response_format_error(message_dict)

        else:
            response_dict = response_format_error(form.format_validate_response())
            #response_dict = errors #response_format_error("Formulário com dados inválidos.")
        return HttpResponse(json.dumps(response_dict))

    def save_number(request):
        print("Ja to vindo na API Do save Tel")
        return HttpResponse(json.dumps({}))

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

