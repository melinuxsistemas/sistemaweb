from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from modules.core.models import NaturezaJuridica, EconomicActivity
from modules.core.working_api import WorkingApi, WorkingManager
from django.http.response import Http404


@login_required
def configure_environment(request):
    if len(NaturezaJuridica.objects.all()) == 0:
        NaturezaJuridica().create_initial_database()

    if len(EconomicActivity.objects.all()) == 0:
        EconomicActivity().create_initial_database()
    return render(request, "core/configure_enterprise_environment.html")

@login_required
def index(request):
    return render(request,"base_page.html")


def working(request):
    if request.is_ajax():
        if "unit/frontend/run_test.html" in request.GET['request_page']:
            result = WorkingManager().register_test_front()
            return result
        else:
            return WorkingManager().register_programming_frontend(request.GET['request_page'])
    else:
        raise Http404