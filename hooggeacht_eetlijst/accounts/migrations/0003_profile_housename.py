# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20171025_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='housename',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
