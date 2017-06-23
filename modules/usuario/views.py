from conf import configuration
from modules.usuario.forms import FormRegister, FormLogin, FormChangePassword, FormResetPassword, FormActivationCode, \
    FormConfirmRegister
from modules.usuario.models import Usuario
from modules.core.utils import decode_activation_code, encode_hash_email, send_email,generate_random_password
from django.contrib.auth import logout, login
from django.shortcuts import render, HttpResponseRedirect, redirect
from datetime import datetime, timedelta


def register_page(request):
    form_register = FormRegister()
    return render(request, "usuario/register/register.html", {'formulario_register': form_register})


def register_confirm_page(request, email):
    form = FormConfirmRegister()
    return render(request, "usuario/register/register_confirm.html",{'formulary_confirm_register': form, 'email': email})


def profile_page(request):
    form_change_password = FormChangePassword()
    return render(request, "usuario/profile.html",{'form_change_password':form_change_password})




def activate_user(request, email, activation_code):
    activation_form = FormActivationCode({'activation_code': activation_code})
    user = Usuario.objects.get_user_email(email)

    if check_valid_activation_code(email, activation_code) and user is not None:
        user.activation_code = activation_code
        user.account_activated = True
        try:
            user.save()
            login(request, user)
            return redirect("/system/environment")
        except:
            return render(request, "usuario/register/register_error.html", {'email_activate': email})
    else:
        return render(request, "usuario/register/register_error.html", {'email_activate': email})


def check_valid_activation_code(email,activation_code):
    email_code, date_code = decode_activation_code(activation_code)
    hash_email_test = encode_hash_email(email)
    current_date = datetime.now()
    email_code_is_valid = email_code == hash_email_test
    activation_code_is_unique = Usuario.objects.activation_code_is_unique(activation_code)
    date_code_is_expired = date_code > (current_date + timedelta(1))

    if email_code_is_valid and activation_code_is_unique and not date_code_is_expired:
        return True
    else:
        return False


def reset_password_page(request):
    form = FormResetPassword()
    return render(request, "usuario/reset_password.html", {'formulario_send': form})


def login_page(request):
    form = FormLogin()
    return render(request,"usuario/login.html",{'formulario_login': form})


def logout_page(request):
    logout(request)
    return redirect("/login")