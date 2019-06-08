import hashlib
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManger

from core.models import (DateTimeModel,
                         DeletedModel)


class UserInfo(AbstractBaseUser,
               DateTimeModel,
               DeletedModel,
               models.Model):

    DISPLAY_FIELD = ("id", "username", "age",
                     "phone", "email", "role",
                     "created", "modified")

    CHOICE_ROLE = (
        (1, 'admin'),
        (2, 'user'),
        (3, 'guest')
    )

    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        verbose_name="用户id",
        help_text="用户id")
    username = models.CharField(
        unique=True,
        max_length=64,
        null=False,
        verbose_name="用户名",
        help_text="用户名")
    password = models.CharField(
        max_length=64,
        null=False,
        verbose_name="密码",
        help_text="密码")
    age = models.IntegerField(
        default=18,
        verbose_name="年龄",
        help_text="年龄")
    phone = models.CharField(
        max_length=32,
        default="123456",
        verbose_name="手机号",
        help_text="手机号")
    email = models.CharField(
        max_length=32,
        verbose_name="邮箱",
        help_text="邮箱")
    role = models.IntegerField(
        choices=CHOICE_ROLE,
        default=3,
        verbose_name="用户角色",
        help_text="用户角色")

    # objects = models.Manager()
    objects = UserManger()

    # 唯一标识符的字段名
    USERNAME_FIELD = "username"

    # def get_password(self, pwd):
    #     if not pwd:
    #         return self.password
    #     return (hashlib
    #             .md5(pwd.encode("utf-8"))
    #             .hexdigest())
    #
    # def check_password(self, pwd):
    #     print("pwd:", pwd)
    #     print("pwd:", self.password)
    #     print("pwd:", self.get_password(pwd))
    #     if self.get_password(pwd) == self.password:
    #         return True
    #     return False

    class Meta:
        db_table = "career_account_userinfo"
        verbose_name = "用户表"
        ordering = ['-id']
        get_latest_by = ['created']
        # managed = False
