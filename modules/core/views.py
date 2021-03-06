from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from modules.core.models import NaturezaJuridica, EconomicActivity
from modules.core.working_api import WorkingApi, WorkingManager
from django.http.response import Http404

from modules.entity.permissions import EntityPermissions
from modules.user.models import User, Permissions


@login_required
def index(request):
    return render(request,"base_page.html")


@login_required
def configure_environment(request):
    if len(NaturezaJuridica.objects.all()) == 0:
        NaturezaJuridica().create_initial_database()

    if len(EconomicActivity.objects.all()) == 0:
        EconomicActivity().create_initial_database()
    return render(request, "core/configure_enterprise_environment.html")


@login_required
def system_configurations(request):
    return render(request, "core/configurations/backup/configurations.html")


def access_denied(request):
    return render(request, "error/access_denied.html")


def working(request):
    if request.is_ajax():
        if "unit/frontend/run_test.html" in request.GET['request_page']:
            result = WorkingManager().register_test_front()
            return result
        else:
            return WorkingManager().register_programming_frontend(request.GET['request_page'])
    else:
        raise Http404