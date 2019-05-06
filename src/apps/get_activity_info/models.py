#-*- coding:utf-8 -*-
from django.db import models


class SignUpInfo(models.Model):
    id = models.AutoField(primary_key=True)
    stu_name = models.CharField('姓名', max_length=20)
    stu_class = models.CharField('班级', max_length=20)
    stu_id = models.CharField('学号', max_length=12)
    stu_status = models.CharField('参与身份', max_length=20)
    act_name = models.CharField('活动名称', max_length=20)
    act_score = models.IntegerField('活动分数', default=2)
    act_time = models.DateField('活动时间')

    def __str__(self):
        return self.stu_name

    class Meta:
        unique_together = (("stu_id", "act_name", "stu_status"), )
        managed = False
        db_table = 'activity_registration'
        verbose_name_plural = "报名信息"
        verbose_name = "报名记录"


class ParticipationRecord(models.Model):
    id = models.AutoField(primary_key=True)
    stu_name = models.CharField('姓名', max_length=20)
    stu_class = models.CharField('班级', max_length=20)
    stu_id = models.CharField('学号', max_length=12)
    stu_status = models.CharField('参与身份', max_length=20)
    act_name = models.CharField('活动名称', max_length=20)
    act_score = models.IntegerField('活动分数', default=2)
    act_time = models.DateField('活动时间')
    stu_rank = models.CharField('名次', max_length=20, blank=True, null=True)

    def __str__(self):
        return self.stu_name

    class Meta:
        managed = False
        db_table = 'participationr_record'
        verbose_name_plural = "参与信息"
        verbose_name = "参与记录"

