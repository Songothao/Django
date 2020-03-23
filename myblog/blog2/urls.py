from django.conf.urls import url

from . import  views

urlpatterns = [
    url(r'^index/$', views.index),    #空的要添加$约束
]