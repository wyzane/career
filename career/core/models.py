from django.db import models


class DateModel(models.Model):
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