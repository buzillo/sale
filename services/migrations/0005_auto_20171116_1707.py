# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_service_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description2',
            field=models.TextField(default='', max_length=2000, verbose_name='Описание услуги блок 2'),
        ),
        migrations.AddField(
            model_name='service',
            name='description3',
            field=models.TextField(default='', max_length=2000, verbose_name='Описание услуги блок 3'),
        ),
        migrations.AddField(
            model_name='service',
            name='description4',
            field=models.TextField(default='', max_length=2000, verbose_name='Описание услуги блок 4'),
        ),
        migrations.AddField(
            model_name='service',
            name='description5',
            field=models.TextField(default='', max_length=2000, verbose_name='Описание услуги блок 5'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(default='', max_length=2000, verbose_name='Описание услуги блок 1'),
        ),
    ]