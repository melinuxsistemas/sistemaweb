from django.conf.urls import url
from modules.core.api import ConfigurationsController


urlpatterns = [
    url(r'configurations/backup$', ConfigurationsController().load_backups),
    url(r'configurations/backup/create$', ConfigurationsController().create_backup),
    url(r'configurations/backup/restore$', ConfigurationsController().restore_backup),

]
