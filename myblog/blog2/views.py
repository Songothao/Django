from django.shortcuts import render
from django.http import  HttpResponse
# 执行响应的代码模块（代码逻辑处理的主要地点）

def index(request):
    return render(request, 'blog2/index.html')