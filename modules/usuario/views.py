from modules.usuario.forms import FormRegister, FormLogin, FormChangePassword, FormConfRegister
from modules.core.utils import valida_chave, gera_hash_md5, envia_email
from django.contrib.auth import logout
from django.shortcuts import render
from datetime import datetime, timedelta

def profile_page(request):
    form_change_password = FormChangePassword()
    return render(request, "usuario/profile.html",{'form_change_password':form_change_password})


def register_page(request):
    form_register = FormRegister()
    return render(request, "usuario/register.html", {'formulario_register': form_register})

def confirm_register_page(request):
    form_confirm_reg = FormConfRegister()
    return render(request, "usuario/confirm_register.html", {'formulario_conf_register': form_confirm_reg})

def activate_register_page(request,email,chave):
    hash_chave = gera_hash_md5(email)
    chave_register,data_register = valida_chave(chave)
    data_atual = datetime.now()

    if chave_register != hash_chave or (chave_register == hash_chave and data_register > data_atual+timedelta(1)):
        return render(request, "usuario/register_error.html", {'email_activate': email })

    return render(request, "usuario/activate_register.html", {'email_activate': email,'chave_register': chave })

def new_register_page(request,email):
    envia_email(email)

    return render(request, "usuario/email_ok.html", {'email_activate': email })

def login_page(request):
    form = FormLogin(request.POST)
    return render(request,"usuario/login.html",{'formulario_login': form})


def logout_page(request):
    form = FormLogin()
    logout(request)
    return render(request,"usuario/login.html",{'formulario_login': form})

