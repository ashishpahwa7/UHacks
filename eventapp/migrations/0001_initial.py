# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 20:19
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
            name='college',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_number', models.BigIntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=50)),
                ('field', models.CharField(default='Technical', max_length=20)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.college')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('st_name', models.CharField(max_length=50)),
                ('enroll_no', models.BigIntegerField(primary_key=True, serialize=False)),
                ('course', models.CharField(choices=[('a', 'BCA'), ('b', 'MCA'), ('c', 'BA LLB'), ('d', 'BBA LLB'), ('e', 'LL.M'), ('f', 'Eco. Hons.'), ('g', 'BA(JMC)'), ('h', 'BBA'), ('i', 'BBA(B&I)'), ('j', 'B.Com(H)')], max_length=1)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_number', models.BigIntegerField()),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.college')),
                ('st_society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.society')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_number', models.BigIntegerField()),
                ('enroll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.student')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]