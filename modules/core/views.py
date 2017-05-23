from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from modules.core.working_api import WorkingApi
from django.http.response import Http404


@login_required
def index(request):
    return render(request,"base_page.html")


def working(request):
    if request.is_ajax():
        working_api = WorkingApi()
        return working_api.register_programming(request)
    else:
        raise Http404