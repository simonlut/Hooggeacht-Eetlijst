# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-02 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_posteater_eat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteater',
            name='attachment_eater',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Attachment'),
        ),
    ]
