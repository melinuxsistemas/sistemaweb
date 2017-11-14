from django.conf.urls import url
from modules.core.api import ConfigurationsController


urlpatterns = [
    url(r'configurations/backups$', ConfigurationsController().load_backups),

]
