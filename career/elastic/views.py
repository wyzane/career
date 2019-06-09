from django.views import View

from core.mixins import ResponseMixin
from core.utils import Validator

from .utils import ESHandler


class IndexList(ResponseMixin, View):
    """elastic search索引列表
    """

    def post(self, request):
        es = ESHandler()
        status, index = es.index_list()
        if status != 0:
            self.code = "00007"
            self.status = False
            self.message = "获取索引列表失败"
            return self.get_json_response()
        return self.get_json_response()


class IndexCreation(ResponseMixin, View):
    """创建索引
    """

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        index = validator.arg_check(
            arg_key="index",
            arg_type=str,
            nullable=False)
        alias = validator.arg_check(
            arg_key="alias",
            arg_type=str,
            nullable=False)
        mappings = validator.arg_check(
            arg_key="mappings",
            arg_type='json',
            nullable=False)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            es = ESHandler()
            msg = es.index_create(index, alias, mappings)
            if msg:
                self.code = "00007"
                self.status = False
                self.message = msg
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_json_response()


class IndexRebuild(ResponseMixin, View):
    """重建索引
    """

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        old_index = validator.arg_check(
            arg_key="oldIndex",
            arg_type=str,
            nullable=False)
        new_index = validator.arg_check(
            arg_key="newIndex",
            arg_type=str,
            nullable=False)
        alias = validator.arg_check(
            arg_key="alias",
            arg_type=str)
        mappings = validator.arg_check(
            arg_key="mappings",
            arg_type='json',
            nullable=False)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            es = ESHandler()
            msg = (es.index_rebuild(old_index,
                                    new_index,
                                    alias,
                                    mappings))
            if msg:
                self.code = "00007"
                self.status = False
                self.message = msg
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_json_response()



