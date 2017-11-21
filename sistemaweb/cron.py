import os
from django.core import management
from django.conf import settings
from libs.backup.backup import BackupManager
from django_cron import CronJobBase, Schedule

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistemaweb.settings")

class Backup(CronJobBase):
    RUN_AT_TIMES = ['15:20', '18:00']
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'sistemaweb.Backup'
    print('olá1')

    def __init__(self):
        directory = settings.DBBACKUP_STORAGE_OPTIONS['location']
        if not os.path.exists(directory):
            os.makedirs(directory)
            print('olá2')

    def do(self):
        print('olá3')
        backup = BackupManager().create_backup()
        print(backup)
        #management.call_command('dbbackup')