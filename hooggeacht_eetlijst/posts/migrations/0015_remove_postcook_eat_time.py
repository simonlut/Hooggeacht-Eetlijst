# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-03 11:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20180103_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcook',
            name='eat_time',
        ),
    ]
