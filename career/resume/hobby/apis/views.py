from django.views import View
from django.core.paginator import Paginator

from ..models import Hobby

from core.mixins import ResponseMixin
from core.utils import Validator
from core.constants import (PAGE_SIZE,
                            PAGE_INDEX)


class HobbyList(ResponseMixin, View):
    """兴趣列表视图
    """

    hobby = Hobby.objects
    hobby_extend = Hobby.objects_extend

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        search_desc = validator.arg_check(
            arg_key="searchDesc",
            arg_type=str)
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
            if search_desc:
                hobby_objs = (self.hobby_extend
                              .filter(desc__contains=search_desc)
                              .values(*Hobby.DISPLAY_FIELDS))
            else:
                hobby_objs = (self.hobby_extend
                              .values(*Hobby.DISPLAY_FIELDS))

            paginator = Paginator(hobby_objs, page_size)
            page_info = {
                "pageSize": page_size,
                "pageIndex": page_index,
                "itemTotal": paginator.count,
                "pageTotal": paginator.num_pages
            }
            data = list(paginator
                        .page(page_index)
                        .object_list)
            return self.get_response(data, **page_info)
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_response()


class HobbyDetail(ResponseMixin, View):
    """兴趣详情视图
    """

    hobby = Hobby.objects
    hobby_extend = Hobby.objects_extend

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        hobby_id = validator.arg_check(
            arg_key="hobbyId",
            arg_type=int,
            nullable=False)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            hobby_obj = (self.hobby_extend
                         .filter(id=hobby_id)
                         .values(*Hobby.DISPLAY_FIELDS))
            data = list(hobby_obj)
            return self.get_response(data)
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_response()



