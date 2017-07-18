from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from modules.entity.forms import FormEntity


@login_required()
def entity_page(request):
    form_entity = FormEntity()
    return render(request, "entidade/entidade.html",{'formulario_entidade':form_entity})

def register_entity(request):
    return render(request, "entidade/adicionar_entidade.html")