from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from modules.core.working_api import WorkingManager
from modules.entity.forms import FormPersonEntity, FormCompanyEntity, FormRegisterPhone


@login_required()
def register_entity(request,entity_type):
    print("TO AQUI!!", request.POST, entity_type)
    form_number = FormRegisterPhone()
    if entity_type == 'person':
        form_entity = FormPersonEntity()
        template_url = "entity/register_person.html"
    elif entity_type == 'company':
        form_entity = FormCompanyEntity()
        template_url = "entity/register_company.html"
    else:
        raise Http404

    return render(request, template_url, {'form_entity':form_entity , 'form_register_number': form_number})


'''def entity_page(request):
    #controlador da pg inicial da Entidade
    return render(request, "entity/entity.html")'''
