# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-02 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posteater_attachment_eater'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteater',
            name='extra_eater_allergy',
            field=models.CharField(blank=True, default=0, max_length=124),
        ),
        migrations.AlterField(
            model_name='posteater',
            name='extra_eater_veg',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='posteater',
            name='extra_eaters',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
    ]