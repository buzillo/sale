# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20171114_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='tipeeng',
            field=models.CharField(choices=[('uБензиновый', 'uБензиновый'), ('Дизельный', 'Дизельный')], default='Бензиновый', max_length=200, verbose_name='Тип двигателя'),
        ),
    ]
