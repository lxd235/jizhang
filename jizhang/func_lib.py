#coding:utf-8
from jizhang.models import Category

def sorted_categories(username):
    result=[]
    categories=Category.objects.filter(user__username=username).filter(p_category=None).all()
    result=find_son(categories)
    return result
    
def find_son(sort_list):
    result_list=[]
    for i in sort_list:
        result_list.append(i)
        if i.childs.exists():
            result_list.extend(find_son(i.childs.all()))
    return result_list



def auto_gen_categories(user):
    #工作收入
    new_category=Category(name=u'工作收入',isincome=True,user=user)
    new_category.save()
    sub_category=Category(name=u'工资收入',isincome=True,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'奖金收入',isincome=True,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'股票收入',isincome=True,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'其它收入',isincome=True,user=user,p_category=new_category)
    sub_category.save()
    
    #餐饮
    new_category=Category(name=u'餐饮',isincome=False,user=user)
    new_category.save()
    sub_category=Category(name=u'早餐',isincome=False,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'午餐',isincome=False,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'晚餐',isincome=False,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'水果',isincome=False,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'其它',isincome=False,user=user,p_category=new_category)
    sub_category.save()

    #交通
    new_category=Category(name=u'交通',isincome=False,user=user)
    new_category.save()
    sub_category=Category(name=u'公交',isincome=False,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'地铁',isincome=False,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'的士',isincome=False,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'火车',isincome=False,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'其它',isincome=False,user=user,p_category=new_category)
    sub_category.save()

    #购物
    new_category=Category(name=u'购物',isincome=False,user=user)
    new_category.save()
    sub_category=Category(name=u'服装',isincome=False,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'日用品',isincome=False,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'零食',isincome=False,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'其它',isincome=False,user=user,p_category=new_category)
    sub_category.save()
    
    #医疗
    new_category=Category(name=u'医疗',isincome=False,user=user)
    new_category.save()
    sub_category=Category(name=u'门诊',isincome=False,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'医院',isincome=False,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'买药',isincome=False,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'保健品',isincome=False,user=user,p_category=new_category)
    sub_category.save()
    sub_category=Category(name=u'其它',isincome=False,user=user,p_category=new_category)
    sub_category.save()