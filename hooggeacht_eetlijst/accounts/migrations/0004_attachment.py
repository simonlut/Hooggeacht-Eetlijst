# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 18:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_profile_housename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at_first_name', models.CharField(blank=True, max_length=30)),
                ('at_last_name', models.CharField(blank=True, max_length=30)),
                ('at_veg', models.NullBooleanField()),
                ('at_allergy', models.CharField(blank=True, max_length=100, null=True)),
                ('attachment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
