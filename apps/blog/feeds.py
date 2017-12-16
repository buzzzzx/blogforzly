# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/12/13 下午2:39'

from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from .models import Post


class AllPostsRssFeed(Feed):
    title = "My blog"
    link = '/'
    description = "New posts of my blog."

    def items(self):
        return Post.objects.all().order_by('-created_time')[:5]

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return truncatewords(item.body, 30)
