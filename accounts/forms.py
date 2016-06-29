#coding:utf-8
from django import forms
from django.contrib.auth.models import User
import re
from django.contrib.auth import authenticate

alnum_re=re.compile(r'^[\w^_]{6,12}$')

class Register_forms(forms.Form):

        username=forms.CharField(
                label='Username',
                max_length=100,
                required=True,
                widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Username'})            
        )
        password=forms.CharField(
                label='Password',
                required=True,
                widget=forms.PasswordInput(attrs={'class':'form-control' ,'placeholder':'Password'}),
                
        )
        password_confirm=forms.CharField(
                label='Password(Again)',
                required=True,
                widget=forms.PasswordInput(attrs={'class':'form-control' ,'placeholder':'Repassword'}),
                
        )
        email=forms.EmailField(
                widget=forms.EmailInput(attrs={'class':'form-control' ,'placeholder':'Email'}),
                required=True,
                
        )


        def clean_username(self):

                if not alnum_re.search(self.cleaned_data['username']):
                        raise forms.ValidationError(u'用户名由数字和子母组成且6到12位')
                flags=User.objects.filter(username__iexact=self.cleaned_data['username']).exists()
                if not flags :
                        return self.cleaned_data['username']
                else:
                      raise forms.ValidationError(u'用户名已被注册，请重新注册')


        def clean_email(self):

                user=User.objects.filter(email__iexact=self.cleaned_data['email'])
                if not user:
                        return self.cleaned_data['email']
                else:
                      raise forms.ValidationError(u'邮箱已经被注册了')

        def clean(self):
                cleaned_data=super(Register_forms,self).clean()
                if cleaned_data.get('password') != cleaned_data.get('password_confirm'):
                    raise forms.ValidationError(u'两次密码必须一致')
                return cleaned_data            
                


class Login_forms(forms.Form):

        username=forms.CharField(
                    label='Username',
                    widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Username'})
               )
        password=forms.CharField(
                    label='Password',
                    widget=forms.PasswordInput(attrs={'class':'form-control' ,'placeholder':'Password'})
               )



        def clean(self):

            cleaned_data=super(Login_forms,self).clean()
            user=User.objects.filter(username=cleaned_data.get('username'))
            username=cleaned_data.get('username')
            password=cleaned_data.get('password')
            if (not password) or (not username) :
                raise forms.ValidationError(u'密码或用户名不能为空')
            if not len(user)>0:
                raise   forms.ValidationError(u'用户名不存在')
            else:
                user = authenticate(username=cleaned_data.get('username'),password=password)
                if user:
                    return cleaned_data
                else:
                    raise forms.ValidationError(u'用户名和密码不匹配')

            
            

