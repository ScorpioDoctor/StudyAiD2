import xadmin
from algorithms.models import Algorithm, AlgorithmBanner


class AlgorithmAdmin(object):
    list_display = ["name", "click_number", "favor_number", "brief", "is_hot", "add_time"]
    search_fields = ['name', "brief",]
    list_editable = ["name", "is_hot", ]
    list_filter = ["click_number", "favor_number", "is_hot", "add_time", "category__name"]
    style_fields = {"detail": "ueditor"}


class AlgorithmBannerAdmin(object):
    list_display = ["algorithm", "image", "index"]


xadmin.site.register(Algorithm, AlgorithmAdmin)
xadmin.site.register(AlgorithmBanner, AlgorithmBannerAdmin)
