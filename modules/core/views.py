from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from modules.core.working_api import WorkingApi, WorkingManager
from django.http.response import Http404


@login_required
def configure_environment(request):
    return render(request, "core/configure_enterprise_environment.html")

@login_required
def index(request):
    return render(request,"base_page.html")


def working(request):
    print("TO VINDO AQUI NESSE CARAI??!")
    if request.is_ajax():
        print("VAMOS VER QUANTAS VEZES VIM AQUI: ")
        if "unit/frontend/run_test.html" in request.GET['request_page']:
            print("VOU REGISTRAR O TEST..")
            result = WorkingManager().register_test_front()
            print("VEJA O QUE VOU ENCAMINHAR COMO RESPOSTA: ", result)
            return result
        else:
            return WorkingManager().register_programming_frontend(request.GET['request_page'])
    else:
        raise Http404