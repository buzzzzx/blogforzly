# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/12/11 下午7:20'

from django.conf.urls import url

from . import views
from blog.feeds import AllPostsRssFeed

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.tag, name='tag'),
    url(r'^all/rss/$', AllPostsRssFeed(), name='rss'),
    url(r'^blog_list/$', views.blog_list, name='blog-list'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
]
