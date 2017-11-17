# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

from libs.default.core import BaseController
from libs.default.decorators import request_ajax_required

from modules.core.api import AbstractAPI
from modules.core.utils import response_format_success, response_format_error, generate_activation_code, generate_random_password
from modules.core.comunications import send_generate_activation_code, resend_generate_activation_code ,send_reset_password
from modules.user.forms import FormRegister, FormLogin, FormChangePassword, FormResetPassword
from modules.user.models import User, Permissions
from django.http import HttpResponse
import json


class UserController(BaseController):

    def login_autentication(self, request):
        return self.login(request, FormLogin)

    def register_user(self, request):
        return BaseController().signup(request, FormRegister)

    @request_ajax_required
    def reset_password(self, request):
        form = FormResetPassword(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email'].lower()
            user = User.objects.get_user_email(email)
            if user is not None:
                if user.account_activated:
                    new_password = generate_random_password(email)
                    user.set_password(new_password)
                    try:
                        user.save()
                        send_reset_password(new_password, email)
                        response_dict = BaseController.notify.success(user, list_fields=['email'])

                    except Exception as erro:
                        print("Erro! Verifique a excecao: ", erro)
                        response_dict = BaseController.notify.error({'email': 'Falha ao gerar nova senha.'})
                else:
                    response_dict = BaseController.notify.error(
                        {'email': 'Usuário não confirmado! Verifique a confirmação no email <br>informado ou clique em reenviar confirmação.'})
            else:
                response_dict = BaseController.notify.error({'email': 'Usuário não cadastrado.'})
        else:
            response_dict = BaseController.get_exceptions(None, form)
        return self.response(response_dict)

    @request_ajax_required
    def resend_activation_code(self, request):
        form = FormResetPassword(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email'].lower()
            user = User.objects.get_user_email(email)
            if user is not None:
                if not user.account_activated:
                    activation_code = generate_activation_code(email)
                    user.activation_code = activation_code
                    user.save()
                    resend_generate_activation_code(email, activation_code)
                    response_dict = BaseController.notify.success(user,['email'])
                else:
                    response_dict = BaseController.notify.error({'email': 'Conta já atividade.'})
            else:
                response_dict = BaseController.notify.error({'email': 'Email não cadastrado.'})
        else:
            response_dict = BaseController.notify.error({'email': 'Email inválido.'})
        return self.response(response_dict)

    @request_ajax_required
    @method_decorator(login_required)
    def change_password(self, request):
        form = FormChangePassword(request.POST)
        if form.is_valid():
            user = request.user
            if user.check_password(form.cleaned_data['old_password']):
                user.change_password(form.cleaned_data['password'])
                auth = User.objects.authenticate(request, email=user.email, password=user.password)
                response_dict = self.notify.success(user, message='Usuário alterado com sucesso.', list_fields=['email'])
            else:
                response_dict = self.notify.error({'email': 'Senha antiga está incorreta.'})
        else:
            response_dict = response_format_error(form.format_validate_response())
            print("VEJA OS ERROS: ",response_dict)
        return self.response(response_dict)

    def register_delete(request, email):
        user = User.objects.get_user_email(email)
        if user is not None:
            user.delete()
            response_dict = response_format_error("Usuario deletado com sucesso.")
        else:
            response_dict = response_format_error("Usuario nao existe.")
        return HttpResponse(json.dumps(response_dict))

    @login_required
    @user_passes_test(lambda u: u.permissions.can_view_entity(), login_url='/error/access_denied',redirect_field_name=None)
    def filter_users(request):
        return BaseController().filter(request, User, extra_fields=['permissions'])



class PermissionAPI(BaseController):
    def load(request, id):
        try:
            user = User.objects.get(email=id)
            permissions = Permissions.objects.get(user=user)
            response_dict = response_format_success(permissions,[
                'id','registration','purchases','sales','services',
                'finances','supervision','management','contabil','others'])
        except:
            response_dict = response_format_error(False)
        return HttpResponse(json.dumps(response_dict))

    def save(request):
        id_user = request.POST['id_user']
        registration = request.POST['registration']
        sales = request.POST['sales']
        purchases = request.POST['purchases']
        services = request.POST['services']
        finances = request.POST['finances']
        supervision = request.POST['supervision']
        management = request.POST['management']
        contabil = request.POST['contabil']
        others = request.POST['others']
        try:
            user = User.objects.get(id=id_user)
            permission = Permissions()
            permission.user = user
            permission.registration = registration
            permission.sales = sales
            permission.purchases = purchases
            permission.services = services
            permission.finances = finances
            permission.supervision = supervision
            permission.management = management
            permission.contabil = contabil
            permission.others = others
            permission.save()
            response_dict = response_format_success(permission,['id','registration','purchases','sales','services','finances','supervision','management','contabil','others'])
        except:
            response_dict = response_format_error(False)
        print('saindo no save, olha o response_dict\n',response_dict)
        return HttpResponse(json.dumps(response_dict))