from django.http import Http404
from django.views.decorators.csrf import requires_csrf_token,ensure_csrf_cookie
from django.shortcuts import render,HttpResponse
from django.core import serializers
from modules.core.utils import executar_operacao
from django.template import RequestContext
import json

from modules.usuario.models import Usuario
from modules.usuario.forms import formulario_register

#ensure_csrf_cookie()
def register_page(request):
    form_register = formulario_register()
    return render(request, "usuario/register.html", {'formulario_register': form_register})


#requires_csrf_token
def register_save(request):
    print("Vindo salvar ",request.POST)
    if request.is_ajax():
        form = formulario_register(request.POST)
        response_dict = {}

        if form.is_valid():
            email = request.POST['email'].lower()
            senha = request.POST['senha']

            if Usuario.objects.verificar_email_disponivel(email):
                usuario = Usuario.objects.criar_usuario_contratante(email,senha)
                response_dict['success'] = True
                response_dict['message'] = ""
                response_dict['data-object'] = serializers.serialize('json',[usuario])
                print("Veja como ficou: ",response_dict['data-object'])
            else:
                response_dict['success'] = False
                response_dict['message'] = "Email já cadastrado."
                response_dict['data-object'] = None
                print ("Email ja existe")

        else:
            print ("Erro! validaçao do formulario deu erro")
            print ("Olha os erros: ",form.errors)
            response_dict['message'] = form.errors




        #usuario =
        #usuario.nome =
        #usuario.descricao = request.POST["descricao"].upper()
        #response_dict = executar_operacao(plano, "save")
        #if response_dict['message'] != True:
        #    response_dict['message'] = serializar_plano(response_dict['message'])
        #"""
        return HttpResponse(json.dumps(response_dict))#
    else:
        raise Http404

    #Sreturn HttpResponse(json.dumps({}))
    #return render_to_response("base_page.html")



def login(request):
    return render("usuario/login.html")