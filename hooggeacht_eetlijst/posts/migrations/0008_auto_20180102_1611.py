# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-02 15:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20180102_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteater',
            name='submit_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='posteater',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique_for_month='submit_time'),
        ),
    ]