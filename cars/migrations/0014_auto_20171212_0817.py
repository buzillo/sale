# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_car_bonus'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='idauto',
            field=models.TextField(default='', max_length=200, verbose_name='ID автомобиля в базе'),
        ),
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, verbose_name='ID страницы'),
        ),
    ]
