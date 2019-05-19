from django.views import View
from django.core.paginator import Paginator

from ..models import Skill

from core.utils import Validator
from core.mixins import ResponseMixin


class SkillList(ResponseMixin, View):
    """技术列表视图
    """

    skill = Skill.objects
    skill_extend = Skill.objects_extend

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        skill_id = validator.arg_check(
            arg_key="skillId",
            arg_type=int,
            nullable=False)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            data = (self.skill
                    .filter(id=skill_id,
                            is_deleted=False)
                    .values(*Skill.DISPLAY_FIELDS)
                    .first())
            return self.get_response(data)
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
            return self.get_response()


class SkillDetail(ResponseMixin, View):
    """技能详情视图
    """

    skill = Skill.objects
    skill_extend = Skill.objects_extend

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        skill_desc = validator.arg_check(
            arg_key="skillDesc",
            arg_type=str)
        page_size = validator.arg_check(
            arg_key="pageSize",
            arg_type=int,
            default=8)
        page_index = validator.arg_check(
            arg_type="pageIndex",
            arg_key=int,
            default=1)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            # todo 此处可以封装成通用方法
            skill_obj = self.skill.filter(is_deleted=False)
            if skill_desc:
                data = (skill_obj
                        .filter(desc__contains=skill_desc))
            else:
                data = skill_obj.all()

            page_info = {
                "pageSize": page_size,
                "pageIndex": page_index,

            }
            paginator = Paginator(list(data), page_size)
            page_info = {
                "pageSize": page_size,
                "pageIndex": page_index,
                "pageCount": paginator.count
            }
            data = paginator.page(page_index)
            return self.get_response(list(data), **page_info)
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
            return self.get_response()
