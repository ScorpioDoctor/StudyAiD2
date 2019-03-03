from rest_framework import serializers

from taxonomies.serializers import CategorySerializer
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Article
        fields = "__all__"


class ArticleCreatesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Article
        fields = ('category', 'tags', 'user', 'title', 'brief', 'content')
