from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets

from .serializers import CategorySerializer
from .models import Category


class CategoryListViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    """
    list:
        分类类目列表数据
    retrieve:
        获取分类类目详情
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('category_type', 'name',)
