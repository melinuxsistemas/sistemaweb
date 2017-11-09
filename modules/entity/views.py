from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from modules.entity.forms import EntityIdentificationForm, EntityPhoneForm, EntityEmailForm


@login_required()
@user_passes_test(lambda u: u.permissions.can_view_entity(), login_url='/error/access_denied',redirect_field_name=None)
def entity_page(request):
    form_phone = EntityPhoneForm()
    form_email = EntityEmailForm()
    form_entity = EntityIdentificationForm()
    return render(request, "entity/entity.html",{'form_entity': form_entity, 'form_register_phone': form_phone, 'form_register_email': form_email})

