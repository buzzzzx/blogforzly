# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/12/14 下午5:24'

from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
