from django.conf.urls import patterns, url
from myblog import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    #items
    url(r'^$',views.home,name='home'),
    #category

)