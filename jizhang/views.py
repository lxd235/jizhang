#coding:utf-8
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from jizhang.models import Category,Item
from jizhang.forms import Newcategory,New_item_form
from jizhang.func_lib import sorted_categories
# Create your views here.


@login_required
def items(request):
    user=request.user
    if request.method=='POST':
        item_id=request.POST.getlist('checkbox')
        item_id=map(lambda x:int(x),item_id)
        if len(item_id)>0:
            for i in item_id:
                item=Item.objects.get(id=i)
                item.delete()
    items=Item.objects.filter(category__user__username=user.username)
    paginator=Paginator(items,12)
    page=request.GET.get('page')
    try:
        items_listt=paginator.page(page)
    except EmptyPage:
        items_list=paginator.page(1)
    except PageNotAnInteger:
        items_list=paginator.page(paginator.num_pages)
    return render(request,'jizhang/items.html',{'items':items_list})


@login_required
def edit_item(request,pk):
    if request.method=='POST':
        form=New_item_form(request,data=request.POST)
        if form.is_valid():
            form.save(id=pk)
            return HttpResponseRedirect('/jizhang/')
        else:
            return render(request,'jizhang/new_item.html',{'form':form})
    instance=Item.objects.get(id=pk)
    form=New_item_form(request,instance=instance)
    return render(request,'jizhang/new_item.html',{'form':form})

@login_required
def new_item(request):
    if request.method=='POST':
        form=New_item_form(request, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/jizhang/')
        else:
            return render(request,'jizhang/new_item.html',{'form':form})
    form=New_item_form(request)
    return render(request,'jizhang/new_item.html',{'form':form})

@login_required
def categories(request):
    user=request.user
    if request.method=='POST':
        cate_id=request.POST.getlist('checkbox')
        cate_id=map(lambda x:int(x),cate_id)
        if len(cate_id)>0:
            for id in cate_id:
                category=Category.objects.get(id=id)
                category.delete()
    categories=sorted_categories(user.username)
    paginator=Paginator(categories,12)
    page=request.GET.get('page')
    try:
        categories_list=paginator.page(page)
    except  PageNotAnInteger:
        categories_list=paginator.page(1)
    except EmptyPage:
        categories_list=paginator.page(paginator.num_pages)

    return render(request,'jizhang/categories.html',{'categories':categories_list})

@login_required
def show_category(request,pk):
    pass

@login_required
def edit_category(request,pk):
    if request.method=='POST':
        form=Newcategory(request,data=request.POST)
        if form.is_valid():
            form.save(id=pk)
            return HttpResponseRedirect('/jizhang/categories/')
        else:
            return render(request,'jizhang/new_category.html',{'form':form})
    instance=Category.objects.get(id=pk)
    form=Newcategory(request,instance=instance)
    return render(request,'jizhang/new_category.html',{'form':form})

@login_required
def new_category(request):
    if request.method=='POST':
        form=Newcategory(request,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/jizhang/categories/')
        else:
            return render(request,'jizhang/new_category.html',{'form':form})
    form=Newcategory(request)
    return render(request,'jizhang/new_category.html',{'form':form})
@login_required
def autocomplete_comments(request):
    pass