from django import forms
from myblog.models import Article
from ckeditor.widgets import CKEditorWidget
from myblog.func_lib import get_result 


class Article_form(forms.ModelForm):

    class Meta:
        model=Article
        fields=('title','content','category')

    def __init__(self,*args,**kwargs):
        super(Article_form, self).__init__(*args, **kwargs)
        self.fields['content'].widget=CKEditorWidget(attrs={'class':'form-control'})
        self.fields['title'].widget=forms.TextInput(attrs={'class':'form-control'})
        choices=[('','----')]+[(i.id,i) for i in get_result()]
        self.fields['category'].widget=forms.Select(choices=choices,attrs={'class':'form-control'})
