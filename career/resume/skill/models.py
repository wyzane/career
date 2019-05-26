from django.db import models

from core.models import (DateTimeModel,
                         DeletedModel)
from core.managers import BaseManager
from .querysets import SkillQuerySet


class Skill(DateTimeModel,
            DeletedModel,
            models.Model):

    DISPLAY_FIELDS = ("id", "desc", "created", "modified")

    id = models.AutoField(
        primary_key=True,
        verbose_name="唯一id",
        help_text="唯一id")
    desc = models.CharField(
        max_length=1024,
        default="",
        verbose_name="技能介绍",
        help_text="技能介绍")

    objects = models.Manager()

    # 扩展django查询方法1：自定义QuerySet
    # as_manager()返回一个Manager实例，并复制了SkillQuerySet中的方法
    objects_extend = SkillQuerySet.as_manager()
    # 或者
    # objects_extend = BaseManager.from_queryset(SkillQuerySet)()

    class Meta:
        db_table = "career_resume_skill"
        verbose_name = "技术栈表"
        ordering = ['-id']
        get_latest_by = ['created']
        # indexes = [
        #     models.Index(fields=['desc']),
        #     models.Index(fields=['desc'], name='desc_idx'),
        # ]
        # index_together = [
        #     ["pub_date", "deadline"],
        # ]
        # unique_together = ['id', 'desc']
        # managed = False
