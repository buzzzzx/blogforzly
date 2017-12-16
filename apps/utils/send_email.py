# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/12/13 下午5:23'

from django.core.mail import send_mail
from zly_blog.settings import EMAIL_FROM


def send(flag, nickname, semail, text, postname=None):
    email_title = ''
    email_body = ''
    email = 'zhuxin_dev@qq.com'
    message = ''
    if flag == 1:
        email_title = '收到博客评论'
        message = "您的文章《{}》收到一个评论。来自（昵称：{}）（邮箱：{}）。评论内容为：{}".format(postname, nickname, semail, text)
        email_body = message
    elif flag == 2:
        email_title = '收到博客留言'
        message = "您收到一个博客留言。来自（昵称：{}）（邮箱：{}）。留言内容为：{}".format(nickname, semail, text)
        email_body = message

    send_mail(email_title, email_body, EMAIL_FROM, [email])
