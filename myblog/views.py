from django.shortcuts import render
from myblog.models import Article,Category
from django.http import HttpResponseRedirect,HttpResponse
from myblog.forms import Article_form
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def home(request):
    articles=Article.objects.all()
    paginator=Paginator(articles,8)
    page=request.GET.get('page')
    try:
        articles=paginator.page(page)
    except EmptyPage:
        articles=paginator.page(1)
    except  PageNotAnInteger:
        articles=paginator.page(paginator.num_pages)
    return render(request,'myblog/home.html',{'articles':articles})

def message(request):
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
    pass
def edit_article(request,page):
    pass