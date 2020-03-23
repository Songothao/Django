from django.db import models

# ORM 与数据库交互，不用书写sql语句
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null = True)     # null = True  允许为空
    # 修改在 admin 管理工具的默认名，返回文章标题
    def __str__(self):
        return self.title