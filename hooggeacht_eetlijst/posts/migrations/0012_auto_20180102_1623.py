# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-02 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20180102_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteater',
            name='title',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
