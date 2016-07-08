from django.shortcuts import render
from myblog.models import Article,Category,Comment_to_me
from django.http import HttpResponseRedirect,HttpResponse
from myblog.forms import Article_form
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def home(request):
    articles=Article.objects.all()
    articles=get_paginator(articles,8,request)
    return render(request,'myblog/home.html',{'articles':articles})

def message(request):
    if request.method=='POST':
        content=request.POST.get('comment_to_me')
        comment_to_me=Comment_to_me(user=request.user,content=content)
        comment_to_me.save()
    comment_list=Comment_to_me.objects.all()
    comment_list=get_paginator(comment_list,20,request)
    return render(request,'myblog/message.html',{'comment_list':comment_list})
        
    return render(request,'myblog/message.html')
def write(request):
    form=Article_form()
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        category=Category.objects.get(id=1)
        article=Article(title=title,content=content,category=category)
        article.save()
        return HttpResponseRedirect('/myblog')
    return render(request,'myblog/write.html',{'form':form})
def article(request,id):
    if request.method=='POST':
        pass
    article=Article.objects.get(id=id)
    if article:
        return render(request,'myblog/article.html',{'article':article})
def edit_article(request,page):
    pass



def get_paginator(obj_list,num,request):
    paginator=Paginator(obj_list,num)
    page=request.GET.get('page')
    try:
        res_list=paginator.page(page)
    except EmptyPage:
        res_list=paginator.page(1)
    except  PageNotAnInteger:
        res_list=paginator.page(paginator.num_pages)
    return res_list