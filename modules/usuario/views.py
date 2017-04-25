from django.http import HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return HttpResponseRedirect('/cadastrar_empresa')