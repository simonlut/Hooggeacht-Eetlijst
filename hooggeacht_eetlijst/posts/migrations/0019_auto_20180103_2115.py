# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-03 20:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_auto_20180103_2112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcook',
            old_name='author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='posteater',
            old_name='author',
            new_name='user',
        ),
    ]