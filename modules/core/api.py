from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404
from django.utils.decorators import method_decorator

from libs.backup.backup import BackupManager
from libs.default.core import BaseController
from modules.core.models import Backup
from modules.user.models import User
from sistemaweb import settings


class ConfigurationsController(BaseController):

    @method_decorator(login_required)
    #user_passes_test(lambda u: u.permissions.can_view_entity(), login_url='/error/access_denied', redirect_field_name=None)
    def load_backups(self, request):
        self.check_available_space(request)
        return BaseController().filter(request, model=Backup)

    def create_backup(self,request):
        self.start_process(request)
        backup_paramters = BackupManager().create_backup()
        backup = Backup()
        backup.backup_file_name = backup_paramters['file_name']
        backup.backup_link = backup_paramters['link']
        backup.backup_size = backup_paramters['size']
        self.get_exceptions(backup, None)
        if self.full_exceptions == {}:
            response_dict = self.execute(backup, backup.save)
        else:
            response_dict = self.notify.error(self.full_exceptions)
        return self.response(response_dict)

    def restore_backup(self,request):
        self.start_process(request)
        backup_paramters = BackupManager().create_backup()
        backup = Backup()
        backup.backup_file_name = backup_paramters['file_name']
        backup.backup_link = backup_paramters['link']
        backup.backup_size = backup_paramters['size']

        self.get_exceptions(backup, None)
        if self.full_exceptions == {}:
            response_dict = self.execute(backup, backup.save)
        else:
            response_dict = self.notify.error(self.full_exceptions)
        return self.response(response_dict)

    def check_available_space(self,request):
        self.start_process(request)
        backup_list = Backup.objects.all()
        total_space = 2000000000 # Bytes
        used_space  = 0
        for item in backup_list:
            used_space = used_space + item.backup_size

        print("ESPACO DE ARMAZENAMENTO: ",used_space,"/",total_space,"(",(used_space/total_space)*100,")")




        backup_paramters = BackupManager().create_backup()
        backup = Backup()
        backup.backup_file_name = backup_paramters['file_name']
        backup.backup_link = backup_paramters['link']
        backup.backup_size = backup_paramters['size']
        self.get_exceptions(backup, None)
        if self.full_exceptions == {}:
            response_dict = self.execute(backup, backup.save)
        else:
            response_dict = self.notify.error(self.full_exceptions)
        return self.response(response_dict)




class AbstractAPI:

    def filter_request(request, formulary=None):
        if request.is_ajax() or settings.DEBUG:
            if formulary is not None:
                form = formulary(request.POST)
                if form.is_valid():
                    return True, form
                else:
                    return False, form
            else:
                return True,True
        else:
            raise Http404