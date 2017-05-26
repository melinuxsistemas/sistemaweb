from modules.usuario.forms import FormRegister, FormLogin, FormChangePassword
from django.contrib.auth import logout
from django.shortcuts import render

#
def profile_page(request):
    form_change_password = FormChangePassword()
    return render(request, "usuario/profile.html",{'form_change_password':form_change_password})


def register_page(request):
    form_register = FormRegister()
    return render(request, "usuario/register.html", {'formulario_register': form_register})


def login_page(request):
    form = FormLogin(request.POST)
    return render(request,"usuario/login.html",{'formulario_login': form})


def logout_page(request):
    form = FormLogin()
    logout(request)
    return render(request,"usuario/login.html",{'formulario_login': form})

