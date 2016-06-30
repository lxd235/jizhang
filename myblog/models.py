#coding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20,verbose_name=u'分类名')
    p_catagory=models.ForeignKey('self',blank=True,null=True,verbose_name='上级分类',related_name='childs')


class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name=u'标题')
    content=models.TextField()
    write_date=models.DateTimeField(auto_now_add=True,verbose_name=u'写作时间')
    change_date=models.DateTimeField(auto_now=True,verbose_name=u'最后修改时间')
    category=models.ForeignKey(Category,verbose_name=u'所属分类')

class Comment_to_me(models.Model):
    user=models.ForeignKey(User,verbose_name=u'用户')
    comment_date=models.DateTimeField(auto_now_add=True,verbose_name=u'评论时间')
    content=models.CharField(max_length=200,verbose_name=u"评论内容")
    

    class Meta:
        ordering=['-comment_date']

class Comment_to_article(Comment_to_me):
    article=models.ForeignKey(Article,verbose_name=u'被评论文章')


class user_profile(models.Model):
    phone_number=models.IntegerField(verbose_name=u'电话')
    level=models.IntegerField(verbose_name=u'等级')
    image=models.ImageField(max_length=150,verbose_name=u'头像')


