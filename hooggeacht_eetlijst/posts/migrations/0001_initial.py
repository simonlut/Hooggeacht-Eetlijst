# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 11:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eat_time', models.DateField()),
                ('food', models.CharField(blank=True, max_length=30)),
                ('extra_eaters', models.PositiveSmallIntegerField(blank=True)),
                ('extra_eater_veg', models.PositiveSmallIntegerField(blank=True)),
                ('extra_eater_allergy', models.CharField(blank=True, max_length=124)),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostEater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_eaters', models.PositiveSmallIntegerField(blank=True)),
                ('extra_eater_veg', models.PositiveSmallIntegerField(blank=True)),
                ('extra_eater_allergy', models.CharField(blank=True, max_length=124)),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]