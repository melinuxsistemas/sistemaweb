from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from modules.entity.forms import EntityIdentificationForm, EntityPhoneForm, EntityEmailForm

"""
@login_required()
def register_entity(request,entity_type):
    form_number = FormPhone()
    form_email = FormEmail()
    if entity_type == 'person':
        form_entity = FormPersonEntity()
        template_url = "entity/register_person.html"
    elif entity_type == 'company':
        form_entity = FormCompanyEntity()
        template_url = "entity/register_company.html"
    else:
        raise Http404
    return render(request, template_url, {'form_entity':form_entity , 'form_register_number': form_number, 'form_register_email':form_email})
"""


@login_required()
def entity_page(request):
    form_phone = EntityPhoneForm()
    form_email = EntityEmailForm()
    form_entity = EntityIdentificationForm()
    return render(request, "entity/entity.html",{'form_entity': form_entity, 'form_register_phone': form_phone, 'form_register_email': form_email})

