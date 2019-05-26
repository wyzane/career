from django.db import models

from .managers import HobbyManager

from core.models import (DateTimeModel,
                         DeletedModel)


class Hobby(DateTimeModel,
            DeletedModel,
            models.Model):

    DISPLAY_FIELDS = ("id", "desc",
                      "created", "modified")

    id = models.AutoField(
        primary_key=True,
        verbose_name="唯一id",
        help_text="唯一id")
    desc = models.CharField(
        max_length=1024,
        verbose_name="兴趣描述",
        help_text="兴趣描述")

    objects = models.Manager()
    objects_extend = HobbyManager()

    class Meta:
        db_table = "career_resume_hobby"
        verbose_name = "兴趣表"
        ordering = ['-id']
        get_latest_by = ['created']
        # managed = False


