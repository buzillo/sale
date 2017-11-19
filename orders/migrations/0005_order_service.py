# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_service_photo'),
        ('orders', '0004_delete_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('phone', models.CharField(max_length=200, verbose_name='Телефон')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Заявка на услугу',
                'verbose_name_plural': 'Заявки на услугу',
            },
        ),
    ]
