from django.views import View

from core.utils import Validator
from core.mixins import ResponseMixin
from ..models import Skill


class SkillCreation(ResponseMixin, View):
    """技能创建视图
    """

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        desc = validator.arg_check(
            arg_key="desc",
            arg_type=str,
            nullable=False)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            skill_obj = Skill.objects.create(desc=desc)
            data = {
                "id": skill_obj.id,
                "desc": skill_obj.desc
            }
            return self.get_json_response(data)
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_json_response()


class SkillUpdate(ResponseMixin, View):
    """技能更新视图
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
        desc = validator.arg_check(
            arg_key="desc",
            arg_type=str)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            skill_obj = (self.skill_extend
                         .update_by_id(skill_id, desc=desc))
            # skill_obj = self.skill.get(id=skill_id)
            if skill_obj:
                data = (skill_obj
                        .values(*Skill.DISPLAY_FIELDS)
                        .first())
                return self.get_json_response(data)
            else:
                self.code = "00002"
                self.status = False
                self.message = err_msg
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_json_response()


class SkillDeletion(ResponseMixin, View):
    """技能删除视图
    """

    skill = Skill.objects
    skill_extend = Skill.objects_extend

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        skill_ids = validator.arg_check(
            arg_key="skillIds",
            arg_type='list',
            nullable=False)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            skill_obj = (self.skill
                         .filter(id__in=skill_ids)
                         .update(is_deleted=True))
            return self.get_json_response()
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_json_response()


class SkillDownload(ResponseMixin, View):
    """技能下载视图
    """
    pass
