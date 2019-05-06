# -*- coding: utf-8 -*-

from django.conf.urls import url
from apps.wechat import views

urlpatterns = [
    url(r'^$', views.weixin_main),
]