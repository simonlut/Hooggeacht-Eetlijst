# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-02 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20180102_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posteater',
            name='title',
        ),
    ]
