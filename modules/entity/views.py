from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required()
def entity_page(request):
    #pg inicial com tabela de entidade
    return render(request, "entidade/entidade.html")

def register_entity(request):
    return render(request, "entidade/adicionar_entidade.html")