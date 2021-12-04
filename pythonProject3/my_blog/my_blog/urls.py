"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
# 记得引入include

from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static
# 存放映射关系的列表
urlpatterns = [
    path('admin/', admin.site.urls),#管理员界面
    # 新增代码，配置app的url
    path('article/', include('article.urls', namespace='article')),#文章路由
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),#用户路由
    path('password-reset/', include('password_reset.urls')),#密码重置
    path('comment/', include('comment.urls', namespace='comment')),
]

#图片配置好了URL路径
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

