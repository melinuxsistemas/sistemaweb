from django.contrib.auth.decorators import login_required

from modules.core.utils import check_valid_activation_code
from modules.user.forms import FormRegister, FormLogin, FormChangePassword, FormResetPassword, FormActivationCode, FormConfirmRegister
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from modules.user.models import User
from modules.user.validators import check_email_format


def register_page(request):
    form_register = FormRegister()
    return render(request, "usuario/register/register.html", {'formulario_register': form_register})


def register_confirm_page(request, email):
    form = FormConfirmRegister()
    if check_email_format(email):
        user = User.objects.get_user_email(email)
        if user is None:
            return render(request, "usuario/register/register_error_unexist_user.html",{'formulary_confirm_register': form, 'email': email})
        else:
            return render(request, "usuario/register/register_confirm.html",{'formulary_confirm_register': form, 'email': email})
    else:
        return render(request, "usuario/register/register_error_invalid_email.html",{'formulary_confirm_register': form, 'email': email})



@login_required()
def profile_page(request):
    form_change_password = FormChangePassword()
    return render(request, "usuario/profile.html",{'form_change_password':form_change_password})


def activate_user(request, email, activation_code):
    activation_form = FormActivationCode({'activation_code': activation_code})
    user = User.objects.get_user_email(email)
    if user is not None:
        if user.activation_code is None:
            if check_valid_activation_code(email, activation_code):
                user.activation_code = activation_code
                user.account_activated = True
                user.save()
                login(request, user)
                print("TUDO CERTO NA ATIVACAO, DIRECIONAR PARA O SISTEMA")
                return redirect("/system/environment")
            else:
                print("CHAVE NAO EH VALIDA")
                return render(request, "usuario/register/register_error_activation_code.html", {'email': email})
        else:
            print("REGISTRO JA ATIVADO")
            return render(request, "usuario/register/register_error_activated_user.html", {'email': email})
    else:
        print("USUARIO NAO EXISTE")
        return render(request, "usuario/register/register_error_unexist_user.html", {'email': email})


def reset_password_page(request):
    form = FormResetPassword()
    return render(request, "usuario/reset_password.html", {'formulario_send': form})


def login_page(request):
    form = FormLogin()
    return render(request,"usuario/login.html",{'formulario_login': form})


def logout_page(request):
    logout(request)
    return redirect("/login")