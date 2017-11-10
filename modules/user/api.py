# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from libs.default.core import BaseController

from modules.core.api import AbstractAPI
from modules.core.utils import response_format_success, response_format_error, generate_activation_code, generate_random_password
from modules.core.comunications import send_generate_activation_code, resend_generate_activation_code ,send_reset_password
from modules.user.forms import FormRegister, FormLogin, FormChangePassword, FormResetPassword
from modules.user.models import User
from django.http import HttpResponse
import json


class UserController(BaseController):

    def login_autentication(self, request):
        return self.login(request, FormLogin)

    def register_user(self, request):
        return BaseController().signup(request, FormRegister)

    def register_delete(request, email):
        user = User.objects.get_user_email(email)
        if user is not None:
            user.delete()
            response_dict = response_format_error("Usuario deletado com sucesso.")
        else:
            response_dict = response_format_error("Usuario nao existe.")
        return HttpResponse(json.dumps(response_dict))

    def generate_new_activation_code(request):
        resultado, form = AbstractAPI.filter_request(request, FormResetPassword)
        if resultado:
            email = request.POST['email'].lower()
            usuario = User.objects.get_user_email(email)
            if usuario is not None:
                if not usuario.account_activated:
                    activation_code = generate_activation_code(email)
                    resend_generate_activation_code(email, activation_code)
                    response_dict = response_format_success(usuario, ['email'])
                else:
                    response_dict = response_format_error("Essa conta já foi ativada.")
            else:
                response_dict = response_format_error("Email não cadastrado.")
        else:
            response_dict = response_format_error("Email com formato inválido.")
        return HttpResponse(json.dumps(response_dict))

    def activate_account(request):
        result, form = AbstractAPI.filter_request(request)
        if result:
            usuario = User.objects.activate_account(True)
            response_dict = response_format_success(usuario, ['account_activated'])
        return HttpResponse(json.dumps(response_dict))

    def reset_password(request):
        resultado, form = AbstractAPI.filter_request(request, FormResetPassword)
        if resultado:
            email = request.POST['email'].lower()
            usuario = User.objects.get_user_email(email)
            if usuario is not None:
                try:
                    nova_senha = generate_random_password(email)
                    usuario.set_password(nova_senha)
                    usuario.save()
                    send_reset_password(nova_senha, email)
                    response_dict = response_format_success(usuario, ['email'])
                except:
                    response_dict = response_format_success(usuario, ['email'])
            else:
                response_dict = response_format_error("Email não cadastrado.")
        else:
            response_dict = response_format_error("Formulário com dados inválidos.")
        return HttpResponse(json.dumps(response_dict))

    @login_required
    def change_password(request):
        #if request.user.is_authenticated():
        #print("OK, O CARA TA AUTENTICADO")
        result, form = AbstractAPI.filter_request(request, FormChangePassword)
        if result:
            usuario = request.user
            if usuario.check_password(form.cleaned_data['old_password']):
                usuario.change_password(form.cleaned_data['password'])
                auth = User.objects.authenticate(request, email=usuario.email, password=usuario.password)
                auth_user = User.objects.get_user_email(usuario.email)
                if auth is not None and usuario.is_active:
                    #login(request, auth_user)
                    pass
                else:
                    response_dict = response_format_error("Não foi possivel autenticar seu usuário<br>com a senha redefinida.")

                response_dict = response_format_success(request.user,"Usuário alterado com sucesso.")
            else:
                response_dict = response_format_error("Erro! Senha antiga está incorreta.")

        else:
            response_dict = response_format_error(form.format_validate_response())
            #print("VEJA OS ERROS: ",response_dict)
        #else:
        #    #response_dict = response_format_error("Erro! Usuario nao autenticado")
        #    return redirect('/login')

        return HttpResponse(json.dumps(response_dict))

class PermissionAPI(BaseController):
    def load(request, id):
        try:
            print("ENTRANDO TRy")
            user = User.objects.get(email=id)
            print("MEI DO TRY")
            permissions = Permissions.objects.get(user=user)
            response_dict = response_format_success(permissions,[
                'id','registration','purchases','sales','services',
                'finances','supervision','management','contabil','others'])
            '''response_dict = {}
            response_dict['user'] = user.id
            response_dict['registration'] = permissions.registration
            response_dict['purchases'] = permissions.purchases
            response_dict['sales']=permissions.sales
            response_dict['services'] = permissions.services
            response_dict['finances'] = permissions.finances
            response_dict['supervision'] = permissions.supervision
            response_dict['management'] = permissions.management
            response_dict['contabil'] = permissions.contabil
            response_dict['others'] = permissions.others'''
        except:
            response_dict = response_format_error(False)
        return HttpResponse(json.dumps(response_dict))