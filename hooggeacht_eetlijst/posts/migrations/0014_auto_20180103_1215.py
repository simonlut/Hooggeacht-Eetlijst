# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-03 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_remove_posteater_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcook',
            name='eat_time',
            field=models.TimeField(),
        ),
    ]