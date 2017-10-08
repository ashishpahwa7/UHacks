# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0007_auto_20171008_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='university',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='img_url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='eventapp.College'),
        ),
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
