from django.shortcuts import render_to_response

def index(request):
    return render_to_response("base_page.html")

def register(request):
    return render_to_response("usuario/register.html")

def login(request):
    return render_to_response("usuario/login.html")