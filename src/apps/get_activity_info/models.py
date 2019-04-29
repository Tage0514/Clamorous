#-*- coding:utf-8 -*-
from django.db import models


class SignUpInfo(models.Model):
    stu_name = models.CharField(max_length=20)
    stu_class = models.CharField(max_length=20)
    stu_id = models.CharField(primary_key=True, max_length=12)
    act_name = models.CharField(max_length=50)
    act_time = models.DateField()
