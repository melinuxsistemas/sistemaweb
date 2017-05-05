from django.contrib.auth import login, authenticate
from django.shortcuts import render, render_to_response, HttpResponse
from django.template import RequestContext
from django.http.response import Http404
from modules.usuario.form import form_login
from django.forms.models import model_to_dict
from modules.usuario.models import Usuario, GerenciadorUsuario

import json

def index(request):
    return render_to_response("base_page.html")

def register(request):
    return render_to_response("usuario/register.html")


def login(request):
    form = form_login()
    return render(request,"usuario/login.html",{'form': form})

def grava_novo(request):
    print(request.POST)
    if request.is_ajax():
        form = form_login(request.POST)
        resultado = validar_formulario(form)
        if resultado:
            usuario = Usuario()
            usuario.email =   form.cleaned_data['email']
            usuario.set_password(form.cleaned_data["senha"])

            response_dict = executar_operacao(usuario,"save")

            response_dict['message'] = str(response_dict['message'])
        return HttpResponse(json.dumps(response_dict))
    else:
        raise Http404

def controle_usuario(request):
    formulario_usuario = form_login()
    return render_to_response(request,"usuario/login.html",
                              {'formulario_usuario' : formulario_usuario})

def validar_formulario(formulario):
    if formulario.is_valid():
        return True
    else:
        for campo in formulario:
            erros = campo.errors.as_data()
            print("Label "+campo.label)
            if erros != []:
                erro = erros[0]
                #print "olha o erro:",erro[0]
                msg = "Erro! "+campo.label.replace(":","")+str(erros[0])
                print(msg)
                return msg



def executar_operacao(registro,operacao):
    response_dict = {}
    if operacao == "save":
        metodo_selecionado = registro.save
        menssage_sucesso = "Registro adicionado com Sucesso!"
        menssage_falha = "Erro! Registro não pode ser Salvo.\n"

    elif operacao == "delete":
        metodo_selecionado = registro.delete
        menssage_sucesso = "Registro apagado com Sucesso!"
        menssage_falha = "Erro! Registro não pode ser Salvo.\n"

    try:
        metodo_selecionado()
        response_dict['success'] = True
        response_dict['message'] = registro.id
        print("Sucesso na execucao")
    except Exception as e:
        response_dict['success'] = False
        response_dict['message'] = menssage_falha+str(e)
        print("falha na execucao")
    print(response_dict)
    return response_dict,registro