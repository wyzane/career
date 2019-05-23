from django.views import View
from django.forms.models import model_to_dict

from ..models import Project

from core.mixins import ResponseMixin
from core.utils import Validator


class ProjectCreation(ResponseMixin, View):
    """项目创建视图
    """

    projects = Project.objects
    projects_extends = Project.objects_extend

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        name = validator.arg_check(
            arg_key="name",
            arg_type=str,
            nullable=False)
        desc = validator.arg_check(
            arg_key="desc",
            arg_type=str,
            nullable=False)
        company = validator.arg_check(
            arg_key="company",
            arg_type=str,
            nullable=False)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            project = {
                "name": name,
                "desc": desc,
                "company": company
            }

            project_obj = self.projects.create(**project)
            if project_obj:
                data = model_to_dict(project_obj)
                return self.get_response(data)
            else:
                self.code = "00004"
                self.status = False
                self.message = "项目创建失败"
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_response()
