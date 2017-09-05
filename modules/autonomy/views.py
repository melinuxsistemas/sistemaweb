from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from modules.autonomy.forms import FormAutonomy


@login_required()
def register_autonomy(request):
    form_autonomy = FormAutonomy()
    template_url = "autonomy/register_autonomy.html"

    return render(request,template_url,{'form_autonomy':form_autonomy})