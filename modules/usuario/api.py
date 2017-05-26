from modules.core.utils import response_format_success, response_format_error
from modules.usuario.forms import FormRegister, FormLogin
from modules.usuario.models import Usuario
from django.contrib.auth import login
from django.http import HttpResponse
from django.http import Http404
import json


class AbstractAPI:

    def filter_request(request, formulary):
        if request.is_ajax():
            form = formulary(request.POST).is_valid()
            if form:
                return True,form
            else:
                return False,form
        else:
            raise Http404


class UsuarioAPI:

    def register_save(request):
        resultado, form = AbstractAPI.filter_request(request,FormRegister)
        if resultado:
            email = request.POST['email'].lower()
            senha = request.POST['senha']

            if Usuario.objects.check_available_email(email):
                usuario = Usuario.objects.criar_usuario_contratante(email,senha)
                response_dict = response_format_success(usuario,['email','joined_date'])
                #envia_email(email)

            else:
                response_dict = response_format_error("Erro! Email já cadastrado.")

        else:
            response_dict = response_format_error("Erro! Formulário com dados inválidos.")

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



