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
    if request.is_ajax():
        return WorkingManager().register_programming_frontend(request.GET['request_page'])
    else:
        raise Http404