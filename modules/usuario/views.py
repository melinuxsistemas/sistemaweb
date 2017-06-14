from modules.usuario.forms import FormRegister, FormLogin, FormChangePassword, FormResetPassword, FormActivationCode
from modules.usuario.models import Usuario
from modules.core.utils import decode_activation_code, encode_hash_email, envia_email,generate_random_password
from django.contrib.auth import logout, login
from django.shortcuts import render, HttpResponseRedirect, redirect
from datetime import datetime, timedelta


def profile_page(request):
    form_change_password = FormChangePassword()
    return render(request, "usuario/profile.html",{'form_change_password':form_change_password})


def register_page(request):
    form_register = FormRegister()
    return render(request, "usuario/register/register.html", {'formulario_register': form_register})

def confirm_valid_email(request,email,chave):
    return redirect('activate_user',email,chave)


def activate_user(request, email, chave):
    activation_form = FormActivationCode({'activation_code': chave})
    user = Usuario.objects.get_user_email(email)

    if check_valid_activation_code(email, chave) and user is not None:
        user.activation_code = chave
        user.account_activated = True
        try:
            user.save()
            login(request, user)
        except:
            print("Erro na ativação da Conta")
        return render(request, "usuario/register/activate.html", {'email_activate': email, 'chave_register': chave})
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





















def new_register_page(request,email):
    envia_email(email)
    return render(request, "usuario/email_ok.html", {'email_activate': email})


def new_password_page(request):
    if request.method == "POST":
       email =  request.POST['email']
       print("Voltou com email ",email)
       nova_senha = generate_random_password(email)

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

