# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='st_society',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eventapp.society'),
        ),
    ]
