from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from modules.core.working_api import WorkingManager
from modules.entity.forms import FormPersonEntity, FormCompanyEntity, FormRegisterPhone, FormRegisterEmailEntity


@login_required()
def register_entity(request,entity_type):
    form_number = FormRegisterPhone()
    form_email = FormRegisterEmailEntity()
    if entity_type == 'person':
        form_entity = FormPersonEntity()
        template_url = "entity/register_person.html"
    elif entity_type == 'company':
        form_entity = FormCompanyEntity()
        template_url = "entity/register_company.html"
    else:
        raise Http404

    return render(request, template_url, {'form_entity':form_entity , 'form_register_number': form_number, 'form_register_email':form_email})

@login_required()
def entity_page(request):
    form_number = FormRegisterPhone()
    form_email = FormRegisterEmailEntity()
    form_entity = FormPersonEntity()
    ''' Por hora so está retornando o form de Pessoa
        if entity_type == 'person':
        form_entity = FormPersonEntity()
        template_url = "entity/register_person.html"
    elif entity_type == 'company':
        form_entity = FormCompanyEntity()
        template_url = "entity/register_company.html"
    else:
        raise Http404'''

    return render(request, "entity/entity.html",{'form_entity': form_entity, 'form_register_number': form_number, 'form_register_email': form_email})
    #return render(request, "entity/entity.html")


