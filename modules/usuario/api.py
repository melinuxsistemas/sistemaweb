from django.shortcuts import render

from modules.core.utils import response_format_success, response_format_error, send_email, generate_random_password, \
    send_reset_password, generate_activation_code, send_generate_activation_code
from modules.usuario.forms import FormRegister, FormLogin, FormChangePassword, FormResetPassword
from modules.usuario.models import Usuario
from django.contrib.auth import login
from django.http import HttpResponse
from django.http import Http404
import json


class AbstractAPI:

    def filter_request(request, formulary=None):
        if request.is_ajax():
            if formulary is not None:
                form = formulary(request.POST)
                if form.is_valid():
                    return True, form
                else:
                    return False, form
            else:
                return True,True
        else:
            raise Http404


class UsuarioAPI:

    def register_delete(request, email):
        user = Usuario.objects.get_user_email(email)
        if user is not None:
            user.delete()
            response_dict = response_format_error("Usuario deletado com sucesso.")
        else:
            response_dict = response_format_error("Usuario nao existe.")
        return HttpResponse(json.dumps(response_dict))

    def register_user(request):
        resultado, form = AbstractAPI.filter_request(request, FormRegister)
        #print("VAMOS LA.. VEJA OS TESTS: ",request.POST)
        if resultado:
            #print("TA VALIDO")
            email = request.POST['email'].lower()
            senha = request.POST['password']
            if Usuario.objects.check_available_email(email):
                #print("EMAIL TA DISPONIVEL")
                usuario = Usuario.objects.create_contracting_user(email, senha)
                if usuario is not None:
                    #print("USUARIO TA AE: ",usuario)
                    activation_code = generate_activation_code(email)
                    send_generate_activation_code(email, activation_code)
                    response_dict = response_format_success(usuario, ['email'])
                else:
                    #print("USUARIO NAO TA CADASTRADO")
                    response_dict = response_format_error("Nao foi possivel criar objeto")
            else:
                #print("EMAIL TA INDISPONIVEL")
                response_dict = response_format_error("Email já cadastrado.")
        else:
            #print("FORMULARIO INCORRETO")
            response_dict = response_format_error("Formulário com dados inválidos.")
        return HttpResponse(json.dumps(response_dict))

    def generate_activation_code(request):
        resultado, form = AbstractAPI.filter_request(request, FormResetPassword)
        if resultado:
            email = request.POST['email'].lower()
            usuario = Usuario.objects.get_user_email(email)
            if usuario is not None:
                if not usuario.account_activated:
                    activation_code = generate_activation_code(email)
                    send_generate_activation_code(email, activation_code)
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
            usuario = Usuario.objects.activate_account(True)
            response_dict = response_format_success(usuario, ['account_activated'])

        return HttpResponse(json.dumps(response_dict))

    def login_autentication(request):
        resultado, form = AbstractAPI.filter_request(request, FormLogin)
        if resultado:
            email = request.POST['email'].lower()
            password = request.POST['password']
            user = Usuario.objects.get_user_email(email=email)
            if user != None:
                if user.account_activated:
                    auth = Usuario.objects.authenticate(request, email=email, password=password)
                    if auth is not None and user.is_active:
                        login(request, user)
                        response_dict = response_format_success(user, ['email'])
                    else:
                        response_dict = response_format_error("Usuário não permitido.")
                else:
                    response_dict = response_format_error("Usuário não confirmado.")
            else:
                response_dict = response_format_error("Usuário não existe.")
        else:
            response_dict = response_format_error("Formulário com dados inválidos.")
        return HttpResponse(json.dumps(response_dict))

    def reset_password(request):
        resultado, form = AbstractAPI.filter_request(request, FormResetPassword)
        print("VEJA OS ERROS",form.errors)
        if resultado:
            email = request.POST['email'].lower()
            print("VEJA O EMAIL:",email)
            usuario = Usuario.objects.get_user_email(email)
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
                auth = Usuario.objects.authenticate(request, email=usuario.email, password=usuario.password)
                auth_user = Usuario.objects.get_user_email(usuario.email)
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

