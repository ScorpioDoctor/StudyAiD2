import xadmin
from .models import Category, Tag


class CategoryAdmin(object):
    list_display = ["name", "category_type", "parent_category", "code", "add_time"]
    list_filter = ["category_type", "parent_category", "add_time"]
    search_fields = ['name', 'description']


class TagAdmin(object):
    list_display = ["name", "add_time"]
    list_filter = ["add_time",]
    search_fields = ['name',]


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)

