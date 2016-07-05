#coding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20,verbose_name=u'分类名')
    p_category=models.ForeignKey('self',blank=True,null=True,verbose_name='上级分类',related_name='childs')

    def __unicode__(self):
        return self.get_level()+self.name

    def get_level(self):
        if self.p_category!=None:
            return '--'+self.p_category.get_level()
        else:
            return ''


class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name=u'标题')
    content=models.TextField()
    write_date=models.DateTimeField(auto_now_add=True,verbose_name=u'写作时间')
    change_date=models.DateTimeField(auto_now=True,verbose_name=u'最后修改时间')
    category=models.ForeignKey(Category,verbose_name=u'所属分类')

    class Meta:
        ordering=['-write_date']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '%s'%(reverse('myblog:article',args=(self.id,)))




class Comment_to_me(models.Model):
    user=models.ForeignKey(User,verbose_name=u'用户')
    comment_date=models.DateTimeField(auto_now_add=True,verbose_name=u'评论时间')
    content=models.CharField(max_length=200,verbose_name=u"评论内容")

    class Meta:
        ordering=['-comment_date']

    def __unicode__(self):
        return self.content

class Comment_to_article(Comment_to_me):
    article=models.ForeignKey(Article,verbose_name=u'被评论文章')


class User_profile(models.Model):
    phone_number=models.IntegerField(verbose_name=u'电话')
    level=models.IntegerField(verbose_name=u'等级')
    image=models.ImageField(max_length=150,verbose_name=u'头像')
    user=models.ForeignKey(User,verbose_name=u'用户')


    def __unicode__(self):
        return self.user



def increase_article():
    c=Category(name='python')
    c.save()
    c1=Category(name='Django',p_catagory=c)
    c1.save()
    content="""这是测试的内容，Django是构建web应用很快的一个工具。
    Django，你可以从概念到启动Web应用程序在几个小时内。Django照顾很多Web开发的麻烦，因此您可以专注于编写您的应用程序，而不需要重新发明轮子。它是免费的和开放源代码。
    """
    article=Article(title=u'用Django构建自己的一个应用',content=content,category=c1)
    article.save()