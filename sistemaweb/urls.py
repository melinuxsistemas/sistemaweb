"""sistemaweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from modules.usuario import views as view_usuario
from modules.core import views as view_core


#from modules import usuario
#from modules.usuario import views

urlpatterns = [
    url(r'^$', view_core.index),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', view_usuario.login_page),
    url(r'^register/$', view_usuario.register_page),

    url(r'^api/usuario/', include('modules.usuario.urls')),

    url(r'^api/working/register/$', view_core.working),
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
