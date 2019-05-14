from django.db import models


class Skill(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name="唯一id",
        help_text="唯一id")
