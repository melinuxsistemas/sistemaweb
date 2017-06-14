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

                ##
                ## PRECISA PROVIDENCIAR UMA FORMA DE FAZER O ENVIO DO EMAIL
                ## EM UMA THREAD SEPARADA PARA QUE O SISTEMA NAO FIQUE AGUARDANDO
                ## A OPERACAO SER CONCLUIDA PARA RETORNAR A PAGINA
                ##
                post_email = envia_email(email)

                if post_email is None:
                    response_dict = response_format_error("Não foi possivel enviar o email de ativação para "+email)
            else:
                response_dict = response_format_error("Email já cadastrado.")
        else:
            response_dict = response_format_error("Erro! Formulário com dados inválidos.")
        return HttpResponse(json.dumps(response_dict))

    def login_autentication(request):
        resultado, form = AbstractAPI.filter_request(request, FormLogin)
        if resultado:
            email = request.POST['email'].lower()
            senha = request.POST['password']
            usuario = Usuario.objects.get_user_email(email=email)
            if usuario != None:
                if usuario.account_activated:
                    usuario = Usuario.objects.authenticate(request, email=email, password=senha)
                    if usuario is not None and usuario.is_active:
                        login(request, usuario)
                        response_dict = response_format_success(usuario, ['email'])
                    else:
                        response_dict = response_format_error("Usuário não permitido.")
                else:
                    response_dict = response_format_error("Usuário não confirmado.")
            else:
                response_dict = response_format_error("Usuário não existe.")
        else:
            print("VEJA OS ERROS: ",form.errors)
            response_dict = response_format_error("Formulário com dados inválidos.")

        return HttpResponse(json.dumps(response_dict))

    def change_password(request):

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
        result, form = AbstractAPI.filter_request(request)
        if result:
            usuario = Usuario.objects.activate_account(True)
            response_dict = response_format_success(usuario, ['account_activated'])

        return HttpResponse(json.dumps(response_dict))