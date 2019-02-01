"""StudyAiD2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

# from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

import xadmin
from StudyAiD2.settings import MEDIA_ROOT
from articles import views as article_views
from taxonomies import views as taxonomy_views

router = DefaultRouter()

# 注册分类系统app相关路由
router.register('categories', taxonomy_views.CategoryListViewSet)


# 注册文章app相关的路由
router.register('articles', article_views.ArticleListViewSet)


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # 配置上传文件的访问处理函数
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # api 认证
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # drf 文档
    re_path(r'^docs/', include_docs_urls(title='人工智能社区')),
    # 路由集合
    path('', include(router.urls)),
]
