#coding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Category(models.Model):

    INCOME_CHOICE=(
        (True,u'收入'),
        (False,u'支出'),
        )
    name=models.CharField(max_length=20,verbose_name=u'类别名称')
    user=models.ForeignKey(User,verbose_name=u'用户名')
    p_category=models.ForeignKey('self',verbose_name=u'父类名',null=True,blank=True,related_name='childs')
    isincome=models.BooleanField(choices=INCOME_CHOICE,verbose_name=u'收入OR支出')


    def __unicode__(self):
        return self.leve()+self.name

    def leve(self):
        if self.p_category!=None:
            return '--'+self.p_category.leve()
        else:
            return ''

    def get_absolute_url(self):
        return '%s' %(reverse('jizhang:edit_category',args=(self.id,)))

    def get_items_url(self):
        return '%s' %(reverse('jizhang:show_category',args=(self.id,)))

    def save(self, *args, **kwargs):
    #form保证了子类不能修改isIncome，只能修改顶级父类的isIncome
    #遍历一遍childs，统一设置isIncome
        for child in self.childs.all():
            if child.isIncome != self.isIncome:
                child.isIncome = self.isIncome
                child.save()              
        super(self.__class__, self).save(*args, **kwargs)


class Item(models.Model):

    price=models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u'金额')
    pub_date=models.DateField(verbose_name=u'日期')
    category=models.ForeignKey(Category,verbose_name=u'所属分类',related_name='items')
    comment=models.CharField(max_length=200,blank=True,verbose_name=u'备注',)

    class Meta:
        ordering=['-pub_date']

    def unicode(self):
        return str(self.price)

    def get_item_url(self):
        return '%s'%(reverse('jizhang:edit_item',args=(self.id,)))

    def git_price(self):
        if self.isincome:
            return self.price  
        else:
            return -1*self.price

    def save(self, *args, **kwargs):
        if self.price<0:
            self.price = -1*self.price
        super(Item, self).save(*args, **kwargs)




def gen_test_data():
    u1=User.objects.create_user(username='xiaozhou',password='zhoubo3923')
    #u1=User.objects.filter(username='xiaozhou')[0]
    u2=User.objects.create_user(username='xiaoweng',password='zhoubo3923')
    #u2=User.objects.filter(username='xiaoweng')[0]
    u_list=[u1,u2]

    for u in u_list:
        c1=Category(name='salary',isincome=True,p_category=None,user=u)
        c1.save()
        c2=Category(name='salary_lp',isincome=True,p_category=c1,user=u)
        c2.save()

        base_salary=2000 if u.username=='xiaozhou' else 1500

        for i in range(10):

            i=Item(price=base_salary*(1.0+i/10.0),category=c2,pub_date='2015-%d-1'%(i+1),comment='gong zi')
            i.save()

