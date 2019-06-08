from django.views import View
from django.forms.models import model_to_dict

from ..models import Hobby

from core.mixins import ResponseMixin
from core.utils import Validator


class HobbyCreation(ResponseMixin, View):
    """兴趣创建视图
    """

    hobby = Hobby.objects
    hobby_extend = Hobby.objects_extend

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        desc = validator.arg_check(
            arg_key="desc",
            arg_type=str,
            nullable=False)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            hobby_field = {
                "desc": desc
            }
            hobby_obj = (self.hobby
                         .create(**hobby_field))
            if hobby_obj:
                data = model_to_dict(hobby_obj)
                return self.get_json_response(data)
            else:
                self.code = "00004"
                self.status = False
                self.message = "兴趣创建失败"
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_json_response()


class HobbyDeletion(ResponseMixin, View):
    """兴趣删除视图
    """

    hobby = Hobby.objects
    hobby_extend = Hobby.objects_extend

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        hobby_id = validator.arg_check(
            arg_key="hobbyId",
            arg_type=str,
            nullable=False)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            hobby_obj = (self.hobby_extend
                         .filter(id=hobby_id))
            if hobby_obj:
                hobby_obj.update(is_deleted=True)
            return self.get_json_response()
        else:
            self.code = "00001"
            self.status = False,
            self.message = err_msg
        return self.get_json_response()


class HobbyUpdate(ResponseMixin, View):
    """兴趣更新视图
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
        desc = validator.arg_check(
            arg_key="desc",
            arg_type=str)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            data = None
            if desc:
                update_field = {
                    "desc": desc
                }
                hobby_obj = (self.hobby_extend
                             .filter(id=hobby_id)
                             .update(**update_field))
                if hobby_obj:
                    hobby_obj = self.hobby.filter(id=hobby_id)
                    data = list(hobby_obj
                                .values(*Hobby.DISPLAY_FIELDS))
            return self.get_json_response(data)
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_json_response()
