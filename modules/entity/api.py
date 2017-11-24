from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.core import serializers
from libs.default.core import BaseController
from libs.default.decorators import validate_formulary
from modules.core.api import AbstractAPI
from modules.core.utils import response_format_success, response_format_error
from modules.entity.forms import EntityPhoneForm, EntityEmailForm, EntityIdentificationForm
from modules.entity.models import Entity, Contact, Email
from django.http import HttpResponse
import json


class EntityController(BaseController):
    """
    Obs: Se o metodo for estatico deve usar o @login_required, se nao usar o @method_decorator(login_required)
    """

    @login_required
    @user_passes_test(lambda u: u.permissions.can_view_entity(), login_url='/error/access_denied', redirect_field_name=None)
    def filter(request):
        return BaseController().filter(request, Entity)

    @login_required
    @user_passes_test(lambda u: u.permissions.can_insert_entity(), login_url='/error/access_denied', redirect_field_name=None)
    def save(request):
        return BaseController().save(request, EntityIdentificationForm)

    @login_required
    @user_passes_test(lambda u: u.permissions.can_update_entity(), login_url='/error/access_denied', redirect_field_name=None)
    def update(request):
        print("VEJA COMO ESTA: ", request.POST)
        return BaseController().update(request, EntityIdentificationForm)

    @method_decorator(login_required)
    def disable(self, request):
        return self.disable(request, Entity)


class ContactController(BaseController):
    @login_required
    def save(request):
        return BaseController().save(request, EntityPhoneForm)


    @method_decorator(login_required)
    def load_tel (self,request):
        return self.filter(request,Contact, queryset=Contact.objects.filter(entity=int(request.POST['id'])))

    @login_required
    def update_tel (request):
        return BaseController().update(request,EntityPhoneForm)

    @login_required
    def delete_tel (request):
        return BaseController().delete(request,Contact,request.POST['id'])

    #APIs para o Email
    @login_required
    def save_email(request):
        return BaseController().save(request, EntityEmailForm)

    @login_required
    def update_email (request):
        return BaseController().update(request,EntityEmailForm)


    def load_email (self, request):
        return self.filter(request, Email, queryset=Email.objects.filter(entity=int(request.POST['id'])))

    @login_required
    def delete_email(request):
        return BaseController().delete(request, Email, request.POST['id'])