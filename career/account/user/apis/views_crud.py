from django.views import View
from django.contrib.auth import (login,
                                 logout,
                                 authenticate)
from django.contrib.auth.hashers import make_password


from ..models import UserInfo

from core.mixins import ResponseMixin
from core.utils import Validator


class Login(ResponseMixin, View):
    """登录视图
    """

    objects = UserInfo.objects

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        username = validator.arg_check(
            arg_key="username",
            arg_type=str,
            nullable=False)
        password = validator.arg_check(
            arg_key="password",
            arg_type=str,
            nullable=False)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            user_obj = authenticate(request,
                                    username=username,
                                    password=password)
            if user_obj:
                login(request, user_obj)
                request.session["username"] = username
                request.session["user_id"] = user_obj.id
            else:
                self.code = "00005"
                self.status = False
                self.message = "登录失败，用户名或密码错误"
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_json_response()


class Logout(ResponseMixin, View):
    """退出视图
    """

    def post(self, request):
        logout(request)
        return self.get_json_response()


class CreateUser(ResponseMixin, View):
    """创建账户视图
    """

    object = UserInfo.objects

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        username = validator.arg_check(
            arg_key="username",
            arg_type=str,
            nullable=False)
        password = validator.arg_check(
            arg_key="password",
            arg_type=str,
            nullable=False)
        age = validator.arg_check(
            arg_key="age",
            arg_type=int)
        phone = validator.arg_check(
            arg_key="phone",
            arg_type=str)
        email = validator.arg_check(
            arg_key="email",
            arg_type=str)
        role = validator.arg_check(
            arg_key="role",
            arg_type=int)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            user_field = {
                "username": username,
                "password": make_password(password),
            }
            check_field = {
                "username": username
            }
            if age:
                user_field["age"] = age
            if phone:
                user_field["phone"] = phone
            if email:
                user_field["email"] = email
            if role:
                user_field["role"] = role
            user = (self.object
                    .create_with_field_check(check_field,
                                             **user_field))

            if user:
                data = (self.object
                        .display_fields(user,
                                        UserInfo.DISPLAY_FIELD))
                return self.get_json_response(data)
            else:
                self.code = "00004"
                self.status = False
                self.message = "用户创建失败"
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_json_response()


class DeletionUser(ResponseMixin, View):
    """删除用户
    """

    objects = UserInfo.objects

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        user_ids = validator.arg_check(
            arg_key="userIds",
            arg_type='list',
            nullable=False)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            user_objs = (self.objects
                         .delete_with_field_check(user_ids))
        else:
            self.code = "00001"
            self.status = False,
            self.message = err_msg
        return self.get_json_response()
