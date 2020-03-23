from django.contrib import admin

from .models import Article         # 将Article添加到admin管理工具

admin.site.register([Article])
