# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/12/12 下午2:17'

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
