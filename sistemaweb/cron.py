import os
from django.core import management
from django.conf import settings
from libs.backup.backup import BackupManager
from django_cron import CronJobBase, Schedule


class Backup(CronJobBase):
    RUN_AT_TIMES = ['14:00', '18:00']
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'sistemaweb.Backup'

    def do(self):
        backup = BackupManager.create_backup()
        print(backup)
        #management.call_command('dbbackup')