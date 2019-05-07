# -*- coding: utf-8 -*-

from django.conf.urls import url
from apps.get_activity_info import views

urlpatterns = [
    #基础信息获取
    url(r'^pai$', views.pose_activity_info),
    url(r'^gai$', views.get_activity_info_base),
    url(r'^gai/(?P<name>\w+)/(?P<time>\w+)/$', views.get_activity_info),
    url(r'^link$', views.activity)
]