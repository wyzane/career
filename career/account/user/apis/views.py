import json

from django.views import View
from django.http import HttpResponse
from django.core.paginator import Paginator

from core.mixins import ResponseMixin
from core.utils import Validator
from core.constants import (PAGE_SIZE,
                            PAGE_INDEX)
from core.export import ResourceUser

from ..models import UserInfo


class UserList(ResponseMixin, View):
    """用户列表视图
    """

    objects = UserInfo.objects

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        page_size = validator.arg_check(
            arg_key="pageSize",
            arg_type=int,
            default=PAGE_SIZE)
        page_index = validator.arg_check(
            arg_key="pageIndex",
            arg_type=int,
            default=PAGE_INDEX)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            user_objs = (self.objects
                         .all()
                         .values(*UserInfo.DISPLAY_FIELD))
            if user_objs:
                paginator = Paginator(user_objs, page_size)
                page_info = {
                    "pageSize": page_size,
                    "pageIndex": page_index,
                    "itemTotal": paginator.count,
                    "pageTotal": paginator.num_pages
                }
                data = list(paginator
                            .page(page_index)
                            .object_list)
            else:
                page_info = {}
                data = []
            return self.get_json_response(data, **page_info)
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_json_response()


class UserExport(ResponseMixin, View):
    """数据导出
    """

    def post(self, request):
        print("-- 1 --")
        resource_user = ResourceUser()
        dataset = resource_user.export()

        # 导出为json数据
        data_json = dataset.json
        data_json = json.loads(data_json)
        return self.get_json_response(data_json)

        # 导出为csv数据
        # data_csv = dataset.csv
        # response = HttpResponse(data_csv, content_type='text/csv')
        # response['Content-Disposition'] = 'attachment; filename="user.csv"'

        # 导出为excel数据
        # response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        # response['Content-Disposition'] = 'attachment; filename="user.xls"'
        # return response



