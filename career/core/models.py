from django.db import models


class PublicModel(models.Model):
    user_id = models.IntegerField(
        default=-1,
        verbose_name="用户id",
        help_text="用户id")

    class Meta:
        abstract = True


class DateTimeModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间",
        help_text="创建时间")

    modified = models.DateTimeField(
        auto_now=True,
        verbose_name="修改时间",
        help_text="修改时间")

    class Meta:
        abstract = True


class DeletedModel(models.Model):
    is_deleted = models.BooleanField(
        default=False,
        verbose_name="是否删除",
        help_text="是否删除")

    class Meta:
        abstract = True
