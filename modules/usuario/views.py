from django.shortcuts import render_to_response

def index(request):
    print("recebi a requisicao")
    return render_to_response("usuario/adicionar_usuario.html")