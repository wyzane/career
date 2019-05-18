# @Author : WZ 
# @Time : 2019/5/17 21:36 
# @Intro :

from django.views import View
from django.http import HttpResponse

from core.utils import Validator
from ..models import Skill


class SkillCreation(View):
    """技能创建接口
    """

    def post(self, request):
        validator = Validator(request.POST)
        print("post param:", request.POST)
        desc = request.POST.get("desc", "")
        skill_obj = Skill.objects.create(desc=desc)
        return HttpResponse(skill_obj)
