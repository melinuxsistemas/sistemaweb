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
    def load(self, request):
        return self.filter(request, Entity)

    '''@method_decorator(login_required)
    def update(self, request):
        return self.update(request, Entity)'''

    """
    @login_required
    def save(request):
        resultado, form = AbstractAPI.filter_request(request, FormPersonEntity)
        entity = Entity()
        entity.form_to_object(form)
        response_dict = {}
        if resultado:
            try:
                entity.save()
                response_dict = response_format_success(entity, ['id','cpf_cnpj','entity_name','entity_type','birth_date_foundation','created_date'])
                #entity.show_fields_value()
            except Exception as e:
                print("VEJA A EXCECAO QUE DEU: ",e)
                response_dict = response_format_error(format_exception_message(entity.model_exceptions))

        else:
            entity.check_validators()
            model_exceptions = format_exception_message(entity.model_exceptions)
            form_exceptions = form.format_validate_response()

            full_exceptions = {}#dict(form_exceptions, **model_exceptions);
            full_exceptions.update(model_exceptions)
            full_exceptions.update(form_exceptions)

            #print("RESPONSE FORM EXCEPTIONS: ", form_exceptions)
            #print("RESPONSE MODEL EXCEPTIONS: ", model_exceptions)
            #print("RESPONSE FULL EXCEPTIONS: ", full_exceptions)
            response_dict = response_format_error(full_exceptions)

        #print("RESPONSE_DICT: ",response_dict)
        return HttpResponse(json.dumps(response_dict))
    """


    @method_decorator(login_required)
    def load_tel (self,request):
        return self.filter(request,Contact, queryset=Contact.objects.filter(entity=int(request.POST['id'])))

    @login_required()
    def update_tel ( request):
        return BaseController().update(request,EntityPhoneForm)

    @login_required
    def delete_tel (request):
        return BaseController().delete(request,Contact,request.POST['id'])

    #APIs para o Email
    @login_required
    def save_email(request):
        return BaseController().save(request, EntityEmailForm)

    def load_email (self, request):
        return self.filter(request, Contact, queryset=Email.objects.filter(entity=int(request.POST['id'])))

    def update_email (request):
        return BaseController().update(request,EntityEmailForm)

    @login_required
    def delete_email(request):
        return BaseController().delete(request, Email, request.POST['id'])