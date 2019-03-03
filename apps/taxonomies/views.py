from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import CategorySerializer, TagSerializer
from .models import Category, Tag


class CategoryListViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
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


class TagsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # authentication_classes = (
    # BasicAuthentication, SessionAuthentication, TokenAuthentication, JSONWebTokenAuthentication)
    # permission_classes = (IsAuthenticated,)