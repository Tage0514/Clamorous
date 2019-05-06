# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-05 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipationRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stu_name', models.CharField(max_length=20, verbose_name='姓名')),
                ('stu_class', models.CharField(max_length=20, verbose_name='班级')),
                ('stu_id', models.CharField(max_length=12, verbose_name='学号')),
                ('stu_status', models.CharField(max_length=20, verbose_name='参与身份')),
                ('act_name', models.CharField(max_length=20, verbose_name='活动名称')),
                ('act_score', models.IntegerField(default=2, verbose_name='活动分数')),
                ('act_time', models.DateField(verbose_name='活动时间')),
                ('stu_rank', models.CharField(blank=True, max_length=20, null=True, verbose_name='名次')),
            ],
            options={
                'verbose_name': '参与记录',
                'verbose_name_plural': '参与信息',
                'db_table': 'participationr_record',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SignUpInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=20, verbose_name='姓名')),
                ('stu_class', models.CharField(max_length=20, verbose_name='班级')),
                ('stu_id', models.CharField(max_length=12, verbose_name='学号')),
                ('stu_status', models.CharField(max_length=20, verbose_name='参与身份')),
                ('act_name', models.CharField(max_length=20, verbose_name='活动名称')),
                ('act_score', models.IntegerField(default=2, verbose_name='活动分数')),
                ('act_time', models.DateField(verbose_name='活动时间')),
            ],
            options={
                'verbose_name': '报名记录',
                'verbose_name_plural': '报名信息',
                'db_table': 'activity_registration',
                'managed': False,
            },
        ),
    ]
