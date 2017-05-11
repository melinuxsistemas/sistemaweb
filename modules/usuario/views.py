from django.shortcuts import render,HttpResponse
from django.http import Http404
import json

from modules.core.utils import response_format_success,response_format_error
from modules.usuario.models import Usuario
from modules.usuario.forms import formulario_register


def register_page(request):
    form_register = formulario_register()
    return render(request, "usuario/register.html", {'formulario_register': form_register})


def register_save(request):
    if request.is_ajax():
        form = formulario_register(request.POST)

        if form.is_valid():
            email = request.POST['email'].lower()
            senha = request.POST['senha']

            if Usuario.objects.check_available_email(email):
                usuario = Usuario.objects.criar_usuario_contratante(email,senha)
                response_dict = response_format_success(usuario,['email','joined_date'])

            else:
                response_dict = response_format_error("Erro! Email já cadastrado.")

        else:
            response_dict = response_format_error("Erro! Formulário com dados inválidos.")

        return HttpResponse(json.dumps(response_dict))#
    else:
        raise Http404

def login_save(request):
    if request.is_ajax():
        form = formulario_login(request.POST)

        if form.is_valid():
            email = request.POST['email'].lower()
            senha = request.POST['senha']

            usuario = authenticate(email=email, password=senha)
            print(usuario)
            if usuario != None:
                if usuario.is_active:
                    print("Você forneceu um email e senha corretos!")
                    login(request, email)
                    response_dict = response_format_success(usuario, ['email', 'joined_date','password'])
                else:
                    print("Email nao cadastrado!")
                    response_dict = response_format_error("Erro! Formulário com dados inválidos.")
            else:
                print("Seu email e senha estavam incorretos.")
                response_dict = response_format_error("email ou senha invalidos.")

        else:
            response_dict = response_format_error("Erro! Formulário com dados inválidos.")

        return HttpResponse(json.dumps(response_dict))
    else:
        raise Http404


def login_page(request):
    form = formulario_login(request.POST)
    return render(request,"usuario/login.html",{'formulario_login': form })