# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20171115_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_service',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]