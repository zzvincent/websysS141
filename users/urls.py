from django.conf.urls import patterns, include, url
from views import * 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'websysS141.views.home', name='home'),
    url(r'^login/', login, name='user_login'),
    url(r'^nearby_list/', nearby_list, name='user_nearby_list'),
    url(r'^fblogin/', fblogin, name='user_fblogin'),
    url(r'^activity/', activity, name='user_activity'),
    url(r'^testpost/', testpost, name='user_testpost'),
    url(r'^testget/', testget, name='user_testget'),
)
