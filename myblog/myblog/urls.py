
from django.contrib import admin
from django.conf.urls import url,include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    url('blog2/', include('blog2.urls')),
]





