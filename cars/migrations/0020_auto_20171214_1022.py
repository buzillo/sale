# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0019_ordercar_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sta', models.CharField(default='', max_length=2000, verbose_name='Выгоды на Rapid')),
            ],
            options={
                'verbose_name': 'СТА',
                'verbose_name_plural': 'СТА',
            },
        ),
        migrations.AlterField(
            model_name='ordercar',
            name='id_car',
            field=models.CharField(max_length=200, verbose_name='ID автомобиля'),
        ),
    ]
