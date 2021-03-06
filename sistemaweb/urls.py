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
from django.contrib import admin
from django.conf.urls import url, include
from modules.core import views as view_core
from modules.user import views as view_usuario
from modules.entity import views as view_entity
from modules.user import views as view_autonomy

handler403 = 'modules.core.views.access_denied'


urlpatterns = [
    url(r'^$', view_core.index),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', view_usuario.login_page),
    url(r'^logout', view_usuario.logout_page),
    url(r'^register/$', view_usuario.register_page),
    url(r'^register/confirm/(?P<email>[^/]+)$', view_usuario.register_confirm_page),
    url(r'^register/activate/(?P<email>[^/]+)/(?P<activation_code>\w{0,46})/$', view_usuario.activate_user),
    url(r'^reset_password/$', view_usuario.reset_password_page),
    url(r'^profile/$', view_usuario.profile_page),

    url(r'^entity/$', view_entity.entity_page),
    url(r'^permissions/$', view_autonomy.register_autonomy),
    url(r'^users/$', view_usuario.user_administration),

    url(r'^api/core/', include('modules.core.urls')),
    url(r'^api/user/', include('modules.user.urls')),
    url(r'^api/entity/', include('modules.entity.urls')),


    url(r'^api/working/register', view_core.working),
    url(r'^system/environment', view_core.configure_environment),
    url(r'^system/configurations', view_core.system_configurations),
    url(r'session_security/', include('session_security.urls')),
    url(r'error/access_denied',view_core.access_denied)

]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
