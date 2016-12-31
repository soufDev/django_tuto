#-*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^article/(\d+)$', views.read, name='read'),

    #url(r'^article/(?P<id_article>\d+)$', views.view_article),
    #url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', views.articles_list),
    #url(r'^redirection$', views.view_redirection, name="redirect_article"),
    #url(r'^date$', views.actual_date),
    #url(r'^addition/(?P<number1>\d+)/(?P<number2>\d+)/$', views.addition),

]