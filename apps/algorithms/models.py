from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField
from taxonomies.models import Category, get_sentinel_category


class Algorithm(models.Model):
    """
    算法
    """
    category = models.ForeignKey(Category, verbose_name="算法类目", on_delete=models.SET(get_sentinel_category))
    serial_number = models.CharField(max_length=50, default="", verbose_name="算法编号")
    name = models.CharField(max_length=100, verbose_name="算法名称")
    click_number = models.IntegerField(default=0, verbose_name="点击数")
    favor_number = models.IntegerField(default=0, verbose_name="收藏数")
    brief = models.TextField(max_length=500, verbose_name="算法简介")
    detail = UEditorField(verbose_name="算法详情", imagePath="algorithms/images/",
                                  width=1000, height=300,filePath="algorithms/files/", default='')
    front_image = models.ImageField(upload_to="algorithms/images/", null=True,
                                              blank=True, verbose_name="算法封面图")
    is_hot = models.BooleanField(default=False, verbose_name="是否热门")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '算法'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class AlgorithmBanner(models.Model):
    """
    轮播的算法
    """
    algorithm = models.ForeignKey(Algorithm, verbose_name="算法", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banners/', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '轮播算法'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.algorithm.name
