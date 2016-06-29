#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from accounts.forms import Register_forms
from accounts.forms import Login_forms
from jizhang.func_lib import auto_gen_categories

# Create your views here.
def index0(request):
        return HttpResponseRedirect('/accounts/login')
@login_required
def index(request):
        username=request.user.username
        return  render(request,'accounts/index.html',{'username':username})
def accounts_logout(request):
        logout(request)
        return  render(request,'accounts/logout.html')
def  accounts_login(request):
                if request.method=='POST':
                        form=Login_forms(request.POST)
                        if form.is_valid():
                                username=form.cleaned_data['username']
                                password=form.cleaned_data['password']
                                user = authenticate(username=username,password=password)
                                if user :
                                        if user.is_active:
                                                login(request,user)
                                                return HttpResponseRedirect('/jizhang/')
                                        else:
                                                return HttpResponse('your password in valid,but the account has been disable')
                                else:
                                        return HttpResponse('your username and password is invalid')
                        else:   
                                return render(request,'accounts/login.html',{'form':form})
                else:
                        form=Login_forms()
                        return  render(request,'accounts/login.html',{'form':form})
def register(request):
        if request.method=='POST':
                form=Register_forms(request.POST)
                if form.is_valid():
                        username=form.cleaned_data['username']
                        password=form.cleaned_data['password']
                        email=form.cleaned_data['email']
                        user=User.objects.create_user(username=username,password=password,email=email)
                        user.save()
                        user1 = authenticate(username=username,password=password)
                        login(request,user1)
                        auto_gen_categories(user)
                        return HttpResponseRedirect('/jizhang/')
                else:
                        return  render(request,'accounts/register.html',{'form':form})
        form=Register_forms()
        return  render(request,'accounts/register.html',{'form':form})
