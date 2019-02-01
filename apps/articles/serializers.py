from rest_framework import serializers

from taxonomies.serializers import CategorySerializer
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Article
        fields = "__all__"
