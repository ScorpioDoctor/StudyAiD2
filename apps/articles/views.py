from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, filters, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from utils.permissions import IsOwnerOrReadOnly
from .filters import ArticleFilter
from .serializers import ArticleSerializer, ArticleCreatesSerializer
from .models import Article


class ArticleListPagination(PageNumberPagination):
    """
    自定义文章列表分页器
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class ArticleListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
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


class ArticleCreatesViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    文章作者对文章的增删改
    """
    queryset = Article.objects.all()
    serializer_class = ArticleCreatesSerializer
    authentication_classes = (BasicAuthentication,SessionAuthentication, TokenAuthentication, JSONWebTokenAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        re_dict = serializer.data
        re_dict['id'] = obj.id
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()
