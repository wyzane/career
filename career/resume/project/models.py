from django.db import models

from core.models import (DateTimeModel,
                         DeletedModel)
from .querysets import ProjectQuerySet


class Project(DateTimeModel,
              DeletedModel,
              models.Model):
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
    objects_extend = ProjectQuerySet.as_manager()

    class Meta:
        db_table = "career_resume_project"
        verbose_name = "开发项目表"
        ordering = ['-id']
        get_latest_by = ['created']
        # managed = False

