from modules.usuario.forms import FormRegister, FormLogin, FormChangePassword, FormResetPassword, FormActivationCode
from modules.usuario.models import Usuario
from modules.core.utils import valida_chave, gera_hash_md5, envia_email,gera_nova_senha
from django.contrib.auth import logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from datetime import datetime, timedelta


def profile_page(request):
    form_change_password = FormChangePassword()
    return render(request, "usuario/profile.html",{'form_change_password':form_change_password})


def register_page(request):
    form_register = FormRegister()
    return render(request, "usuario/register.html", {'formulario_register': form_register})

def confirm_valid_email(request,email,chave):
    return redirect('activate_user',email,chave)

def activate_user(request, email, chave):
    hash_chave = gera_hash_md5(email)
    chave_register,data_register = valida_chave(chave)
    data_atual = datetime.now()
    activation_form = FormActivationCode({'activation_code': chave})

    usuario = Usuario.objects.get_user_email(email)
    chave_existente = Usuario.objects.filter( activation_code = chave )

    if len(chave_existente) > 0 or chave_register != hash_chave or (chave_register == hash_chave and data_register > data_atual+timedelta(1)):
        return render(request, "usuario/register_error.html", {'email_activate': email })
    else:

        if usuario is not None:
            usuario.activation_code = chave
            usuario.account_activated = True
            try:
                usuario.save()
            except:
                print("Erro na ativação da Conta")

        return render(request, "usuario/activate_register.html", {'email_activate': email,'chave_register': chave})


def new_register_page(request,email):
    envia_email(email)
    return render(request, "usuario/email_ok.html", {'email_activate': email})


def new_password_page(request):
    if request.method == "POST":
       email =  request.POST['email']
       print("Voltou com email ",email)
       nova_senha = gera_nova_senha(email)

       print("Nova senha", nova_senha)
       usuario = Usuario.objects.get_user_email(email)
       if usuario is not None:
           usuario.set_password(nova_senha)
           usuario.save()

           return HttpResponseRedirect("/")
    else:
       form = FormResetPassword()
       return render(request, "usuario/reset_password.html", {'formulario_send': form})


def login_page(request):
    form = FormLogin()
    return render(request,"usuario/login.html",{'formulario_login': form})


def logout_page(request):
    form = FormLogin()
    logout(request)
    return render(request,"usuario/login.html",{'formulario_login': form})

