# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'услуга', 'verbose_name_plural': 'услуги'},
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(default='', max_length=2000, verbose_name='Описание услуги'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(default='', max_length=200, verbose_name='Название услуги'),
        ),
    ]
