from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator

from ..models import Project

from core.mixins import ResponseMixin
from core.utils import Validator
from core.constants import PAGE_SIZE, PAGE_INDEX


class ProjectList(ResponseMixin, View):
    """项目列表视图
    """

    projects = Project.objects
    projects_extend = Project.objects_extend

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
                project_objs = (self.projects
                                .filter(is_deleted=False)
                                .filter(Q(name__contains=search_desc) |
                                        Q(desc__contains=search_desc) |
                                        Q(company__contains=search_desc))
                                .values(*Project.DISPLAY_FIELDS))
            else:
                project_objs = (self.projects
                                .filter(is_deleted=False)
                                .values(*Project.DISPLAY_FIELDS))

            paginator = Paginator(project_objs, page_size)
            page_info = {
                "pageSize": page_size,  # 每页条数
                "pageIndex": page_index,  # 当前页数
                "itemTotal": paginator.count,  # 数据总数
                "itemPage": paginator.num_pages  # 分页总数
            }
            data = list(paginator
                        .page(page_index)
                        .object_list)
            return self.get_response(data, **page_info)
        else:
            elf.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_response()

