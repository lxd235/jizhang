from django.conf.urls import url
from accounts import views 





urlpatterns = [
    url(r'^login/',views.accounts_login,name='login'),
    url(r'^logout/',views.accounts_logout,name='logout'),
    url(r'^register/',views.register,name='register'),
    url(r'^index/',views.index,name='index'),
]