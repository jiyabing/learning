# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 05:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterModelTable(
            name='users',
            table='users',
        ),
    ]
