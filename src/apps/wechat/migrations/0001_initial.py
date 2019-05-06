# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-05 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BindWechat',
            fields=[
                ('stu_name', models.CharField(max_length=20, verbose_name='姓名')),
                ('stu_class', models.CharField(max_length=20, verbose_name='班级')),
                ('stu_id', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='学号')),
                ('stu_openid', models.CharField(max_length=50, verbose_name='绑定的微信号')),
            ],
            options={
                'verbose_name': '微信绑定',
                'verbose_name_plural': '微信绑定信息',
                'db_table': 'bind_wechat',
                'managed': False,
            },
        ),
    ]