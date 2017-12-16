# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/12/12 下午8:10'

from django.conf.urls import url

from . import views


app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]