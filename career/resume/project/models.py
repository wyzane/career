from django.db import models

from core.models import (DateTimeModel,
                         DeletedModel)
from .querysets import ProjectQuerySet
from .managers import ProjectManager


class Project(DateTimeModel,
              DeletedModel,
              models.Model):

    DISPLAY_FIELDS = ("id", "name", "desc", "company",
                      "created", "modified")

    id = models.AutoField(
        primary_key=True,
        verbose_name="唯一id",
        help_text="唯一id")
    name = models.CharField(
        max_length=64,
        verbose_name="项目名称",
        help_text="项目名称")
    desc = models.TextField(
        verbose_name="项目描述",
        help_text="项目描述")
    company = models.CharField(
        max_length=64,
        default="",
        verbose_name="项目所在公司名称",
        help_text="项目所在公司名称")

    objects = models.Manager()
    # 扩展django查询方法2：自定义Manager
    objects_extend = ProjectManager()

    class Meta:
        db_table = "career_resume_project"
        verbose_name = "开发项目表"
        ordering = ['-id']
        get_latest_by = ['created']
        # managed = False

