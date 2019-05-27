from django.db import models

from .managers import UserManger

from core.models import (DateTimeModel,
                         DeletedModel)


class User(DateTimeModel,
           DeletedModel,
           models.Model):

    CHOICE_ROLE = (
        (1, 'admin'),
        (2, 'user'),
        (3, 'guest')
    )

    id = models.AutoField(
        primary_key=True,
        verbose_name="用户id",
        help_text="用户id")
    username = models.CharField(
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
        verbose_name="手机号",
        help_text="手机号")
    email = models.CharField(
        max_length=32,
        verbose_name="邮箱",
        help_text="邮箱")
    role = models.IntegerField(
        choices=CHOICE_ROLE,
        default=1,
        verbose_name="用户角色",
        help_text="用户角色")

    objects = models.Manager()
    objects_extend = UserManger()

    class Meta:
        db_table = "career_account_user"
        verbose_name = "用户表"
        ordering = ['-id']
        get_latest_by = ['created']
        # managed = False


