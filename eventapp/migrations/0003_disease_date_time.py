# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 11:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0002_disease'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]