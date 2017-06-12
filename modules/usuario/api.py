from modules.core.utils import response_format_success, response_format_error, envia_email
from modules.usuario.forms import FormRegister, FormLogin, FormChangePassword
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


    def register_save(request):
        resultado, form = AbstractAPI.filter_request(request,FormRegister)
        if resultado:
            email = request.POST['email'].lower()
            senha = request.POST['password']

            if Usuario.objects.check_available_email(email):
                usuario = Usuario.objects.criar_usuario_contratante(email, senha)
                response_dict = response_format_success(usuario, ['email', 'joined_date'])

                if envia_email(email) is None:
                    response_dict = response_format_error("Erro! Não foi possivel enviar email para "+email)

            else:
                response_dict = response_format_error("Erro! Email já cadastrado.")

        else:
            response_dict = response_format_error("Erro! Formulário com dados inválidos."+str(form.errors))

            """
                Erro! Formulário com dados inválidos.

                email
                    Este campo é obrigatório.
                confirm_password
                    Este campo é obrigatório.
                password
                    Este campo é obrigatório.

            string
            """

        return HttpResponse(json.dumps(response_dict))



    def login_autentication(request):
        resultado, form = AbstractAPI.filter_request(request, FormLogin)
        if resultado:
            email = request.POST['email'].lower()
            senha = request.POST['senha']
            usuario = Usuario.objects.authenticate(request, email=email, password=senha)

            if usuario is not None and usuario.is_active:
                login(request, usuario)
                response_dict = response_format_success(usuario, ['email'])
            else:
                response_dict = response_format_error("Erro! Usuário ou senha incorreto.")
        else:
            response_dict = response_format_error("Erro! Formulário com dados inválidos.")

        return HttpResponse(json.dumps(response_dict))

    def change_password(request):
        print("REQUEST: ",request.POST)
        result, form = AbstractAPI.filter_request(request, FormChangePassword)
        if result:
            if request.user.check_password(form.cleaned_data['old_password']):
                request.user.change_password(form.cleaned_data['password'])
                print("SENHA ALTERADA!")
                response_dict = response_format_success(request.user,"Usuário alterado com sucesso.")
            else:
                print("SENHA INCORRETA!")
                response_dict = response_format_error("Erro! Senha antiga está incorreta.")
        else:
            response_dict = response_format_error(form.format_validate_response())

        return HttpResponse(json.dumps(response_dict))

    def activate_account(request):
        print("REQUEST :", request.POST)
        result, form = AbstractAPI.filter_request(request)
        print("Resultado", result)
        if result:
            usuario = Usuario.objects.activate_account(True)
            response_dict = response_format_success(usuario, ['account_activated'])

        return HttpResponse(json.dumps(response_dict))