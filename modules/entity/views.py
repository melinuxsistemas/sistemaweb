from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from modules.entity.forms import FormEntity


@login_required()
def register_entity(request):
    form_entity = FormEntity()
    return render(request, "entity/add_entity.html", {'form_entity':form_entity})


'''def entity_page(request):
    #controlador da pg inicial da Entidade
    return render(request, "entity/entity.html")'''
