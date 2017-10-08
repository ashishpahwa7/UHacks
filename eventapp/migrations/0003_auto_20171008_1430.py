# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 09:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0002_auto_20171008_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='society',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.College'),
        ),
        migrations.AlterField(
            model_name='student',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.College'),
        ),
        migrations.AlterField(
            model_name='student',
            name='st_society',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eventapp.Society'),
        ),
        migrations.AlterField(
            model_name='studentadmin',
            name='enroll_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.Student'),
        ),
    ]