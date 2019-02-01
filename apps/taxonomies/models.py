from datetime import datetime

from django.db import models


class Category(models.Model):
    """
    分类类别
    """
    CATEGORY_TYPE = ((1, "一级类目"),(2, "二级类目"),(3, "三级类目"),)

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别代码", help_text="类别代码")
    description = models.TextField(default="该类别暂无描述信息...", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别",
                                        help_text="父类别", related_name="sub_cat", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "分类类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 某个类别被删除的时候该类别对应的所有实体都将会放到 'DeletedCategory' 这个类别下面
def get_sentinel_category():
    return Category.objects.get_or_create(name='DeletedCategory', category_type=1, parent_category=None)[0]


class Tag(models.Model):
    """
    分类标签
    """
    name = models.CharField(max_length=25, verbose_name='标签名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类标签'
        verbose_name_plural = verbose_name
