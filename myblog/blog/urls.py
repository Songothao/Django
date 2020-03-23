from django.conf.urls import url
from . import  views

urlpatterns = [
    url(r'^index/$', views.index),    #空的要添加$约束
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),       # 正则表达式
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^edit_action/$', views.edit_action, name='edit_action')
]