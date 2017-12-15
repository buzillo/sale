# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_auto_20171207_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='VygodaKodiaq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vygoda_kod', models.CharField(default='', max_length=1000, verbose_name='Выгоды на Kodiaq')),
            ],
            options={
                'verbose_name': 'Выгода на Kodiaq',
                'verbose_name_plural': 'Выгода на Kodiaq',
            },
        ),
        migrations.CreateModel(
            name='VygodaOctavia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vygoda_oct', models.CharField(default='', max_length=1000, verbose_name='Выгоды на Octavia')),
            ],
            options={
                'verbose_name': 'Выгода на Octavia',
                'verbose_name_plural': 'Выгода на Octavia',
            },
        ),
        migrations.CreateModel(
            name='VygodaSuperb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vygoda_sup', models.CharField(default='', max_length=1000, verbose_name='Выгоды на Superb')),
            ],
            options={
                'verbose_name': 'Выгода на Superb',
                'verbose_name_plural': 'Выгода на Superb',
            },
        ),
        migrations.CreateModel(
            name='VygodaYeti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vygoda_yeti', models.CharField(default='', max_length=1000, verbose_name='Выгоды на Yeti')),
            ],
            options={
                'verbose_name': 'Выгода на Yeti',
                'verbose_name_plural': 'Выгода на Yeti',
            },
        ),
    ]