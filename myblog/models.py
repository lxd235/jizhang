#coding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    pass


class Category(models.Model):
    pass






class Comment(models.Model):
    user=models.ForeignKey(User,verbose_name=u'用户')
    comment_date=models.DateTimeField(auto_now_add=True,verbose_name=u'评论时间')
    content=models.CharField(max_length=200,verbose_name=u"评论内容")
    article=models.ForeignKey(Article,verbose_name=u'被评论文章')



    class Meta:
        ordering=['-comment_date']