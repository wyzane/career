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


class ProjectDeletion(ResponseMixin, View):
    """项目删除视图
    """

    projects = Project.objects
    projects_extend = Project.objects_extend

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        project_ids = validator.arg_check(
            arg_key="projectIds",
            arg_type="list",
            nullable=False)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            project_objs = (self.projects_extend
                            .filter(id__in=project_ids))
            project_objs.update(is_deleted=True)
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_response()


class ProjectUpdate(ResponseMixin, View):
    """项目更新视图
    """

    projects = Project.objects
    projects_extend = Project.objects_extend

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        project_id = validator.arg_check(
            arg_key="projectId",
            arg_type=int,
            nullable=False)
        project_name = validator.arg_check(
            arg_key="projectName",
            arg_type=str)
        project_desc = validator.arg_check(
            arg_key="projectDesc",
            arg_type=str)
        project_company = validator.arg_check(
            arg_key="projectCompany",
            arg_type=str)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            project_obj = (self.projects_extend
                           .filter(id=project_id))
            if project_obj:
                update_fields = dict()
                if project_name:
                    update_fields["name"] = project_name
                if project_desc:
                    update_fields["desc"] = project_desc
                if project_company:
                    update_fields["company"] = project_company

                if update_fields:
                    project_obj.update(**update_fields)
                    project_obj = (self.projects_extend
                                   .filter(id=project_id))

                data = list(project_obj
                            .values(*Project.DISPLAY_FIELDS))
                return self.get_response(data)
            else:
                self.code = "00002"
                self.status = False
                self.message = "项目不存在"
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_response()
