# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-27 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0011_event_calendar_not_null'),
        ('posts', '0021_auto_20180113_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteater',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='schedule.Event'),
        ),
    ]
