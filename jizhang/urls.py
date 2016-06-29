from django.conf.urls import patterns, include, url
from jizhang import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #items
    url(r'^$',views.items,name='items'),
    url(r'^(?P<pk>\d+)/edit/$',views.edit_item,name='edit_item'),
    url(r'^new/$',views.new_item,name='new_item'),
    #category
    url(r'^categories/$',views.categories,name='categories'),
    url(r'^category/(?P<pk>\d+)/$',views.show_category,name='show_category'),
    url(r'^category/(?P<pk>\d+)/edit/$',views.edit_category, name='edit_category'),
    url(r'^category/new/$',views.new_category, name='new_category'),
    #ajax
    url(r'^ajax/autocomplete_comments/',views.autocomplete_comments),
)