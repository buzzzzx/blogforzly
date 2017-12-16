# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/12/12 下午1:26'

from django import template

from ..models import Post, Category, Tag
from django.db.models.aggregates import Count


register = template.Library()


# 最新文章
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


# 归档文章
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


# 归类
@register.simple_tag
def get_category():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag
def get_tags():
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
