# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_auto_20171212_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='id_car',
            field=models.CharField(default='', max_length=200, verbose_name='Имя'),
        ),
    ]