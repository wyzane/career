# @Author : WZ 
# @Time : 2019/5/17 21:36 
# @Intro :

from django.views import View
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict

from core.utils import Validator
from core.mixins import ResponseMixin
from ..models import Skill


class SkillCreation(ResponseMixin, View):
    """技能创建接口
    """

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        desc = validator.arg_check(
            arg_key="desc",
            # default="技能介绍",
            arg_type=str)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            skill_obj = Skill.objects.create(desc=desc)
            data = {
                "id": skill_obj.id,
                "desc": skill_obj.desc
            }
            return self.get_response(data)
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
            return self.get_response()
