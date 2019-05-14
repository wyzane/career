from django.db import models

from core.models import (DateTimeModel,
                         DeletedModel)
from .querysets import SkillQuerySet


class Skill(DateTimeModel,
            DeletedModel,
            models.Model):
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
    objects_extend = SkillQuerySet.as_manager()

    class Meta:
        db_table = "career_resume_skill"
        verbose_name = "技术栈表"
        ordering = ['-id']
        get_latest_by = ['created']
        # managed = False
