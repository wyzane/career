from django.views import View

from core.mixins import ResponseMixin

from .utils import ESHandler


class IndexList(ResponseMixin, View):
    """elastic search索引列表
    """
    es = ESHandler()
    index_info = es.index_list()
    print("index:", index_info)


class IndexCreation(ResponseMixin, View):
    """创建索引
    """
    pass


class IndexRebuild(ResponseMixin, View):
    """重建索引
    """
    pass
