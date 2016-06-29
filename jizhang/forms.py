#coding:utf-8
from django import forms
from jizhang.models import Category,Item
from jizhang.func_lib import sorted_categories

class Category_form(forms.ModelForm):

    class Meta:
        model=Category
        fields=('name','p_category','isincome')

    def __init__(self, request, *args, **kwargs):
        super(Category_form, self).__init__(*args, **kwargs)
        self.user=request.user
        self.fields['name'].widget=forms.TextInput(attrs={'class':'form-control','placeholder':'分类名'})
        categories=sorted_categories(self.user.username)
        choices=[('',u'-----------')]+[(i.id,i) for i in categories]
        self.fields['p_category'].widget=forms.Select(attrs={'class':'form-control'},choices=choices)
        self.fields['isincome'].widget=forms.CheckboxInput(attrs={'value':'True'})

    def clean_isincome(self):
        if self.cleaned_data['p_category']:
            if not self.cleaned_data['p_category'].isincome==self.cleaned_data['isincome']:
                raise forms.ValidationError(u'是否和父类收入一致')
        return self.cleaned_data['isincome']

    def save(self,id=None):
        new_category=Category(name=self.cleaned_data['name'],
            user=self.user,
            p_category=self.cleaned_data['p_category'],
            isincome=self.cleaned_data['isincome'],
            id=id)
        new_category.save()




class Newcategory(Category_form):
    pass

class Item_form(forms.ModelForm):
    class Meta:
        model = Item
        fields =('price','pub_date','category','comment')

    def __init__(self,request,*args,**kwargs):
        super(Item_form,self).__init__(*args, **kwargs)
        self.user=request.user
        self.fields['price'].widget=forms.TextInput(attrs={'class':'form-control'})
        categories=sorted_categories(self.user.username)
        choices=[('',u'-----------')]+[(i.id,i) for i in categories]
        self.fields['category'].widget=forms.Select(attrs={'class':'form-control'},choices=choices)
        self.fields['pub_date'].widget=forms.TextInput(attrs={'class':'datepicker form-control'})
        self.fields['comment'].widget=forms.TextInput(attrs={'class':'form-control'})

    def save(self,id=None):
        new_item=Item(price=self.cleaned_data['price'],
            category=self.cleaned_data['category'],
            pub_date=self.cleaned_data['pub_date'],
            comment=self.cleaned_data['comment'],id=id)
        new_item.save()

class New_item_form(Item_form):
    pass

