from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Category, Tag


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = Category
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label="标签名", help_text="标签名", required=True, allow_blank=False, max_length=32,
                                     validators=[UniqueValidator(queryset=Tag.objects.all(), message="标签名已经存在")])
    class Meta:
        model = Tag
        fields = ('name', 'id')
