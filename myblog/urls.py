from django.conf.urls import patterns, url
from myblog import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    #items
    url(r'^$',views.home,name='home'),
    url(r'^message/$',views.message,name='message'),
    url(r'^write/$',views.write,name='write'),
    url(r'^article/(?P<id>\d+)/$',views.article,name='article'),
    url(r'^article/(?P<page>\d+)/edit/$',views.edit_article,name='edit_article'),
    
    
    #catergory

]