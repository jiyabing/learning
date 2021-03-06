# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20180625_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.SmallIntegerField()),
            ],
            options={
                'verbose_name': '夫人',
                'verbose_name_plural': '夫人',
                'db_table': 'wife',
            },
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.SmallIntegerField(verbose_name='年齡'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='郵箱'),
        ),
        migrations.AlterField(
            model_name='author',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='激活狀態'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=10, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publicate_date',
            field=models.DateField(verbose_name='出版時間'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=30, verbose_name='書名'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.CharField(max_length=30, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='city',
            field=models.CharField(max_length=10, verbose_name='所在城市'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='country',
            field=models.CharField(max_length=10, verbose_name='国家'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=10, verbose_name='出版社名'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='website',
            field=models.URLField(verbose_name='网址'),
        ),
    ]
