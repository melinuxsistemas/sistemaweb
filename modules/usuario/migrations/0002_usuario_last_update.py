# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='last_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]