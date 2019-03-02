from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination

from .filters import ArticleFilter
from .serializers import ArticleSerializer
from .models import Article


class ArticleListPagination(PageNumberPagination):
    """
    自定义文章列表分页器
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class ArticleListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    文章列表页, 分页， 搜索， 过滤， 排序
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticleListPagination
    # authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ArticleFilter
    search_fields = ('title', 'brief', 'content')
    ordering_fields = ('click_number', 'favor_number', 'comment_number', 'word_count', 'add_time')