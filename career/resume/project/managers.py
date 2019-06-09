# @Author : WZ 
# @Time : 2019/5/21 14:51 
# @Intro :

from django.db import models

from core.managers import (ExistedManager,
                           CRUDManager)


class ProjectManager(ExistedManager,
                     CRUDManager,
                     models.Manager):
    def get_queryset(self):
        """过滤已删除数据
        """

        return (super()
                .get_queryset()
                .filter(is_deleted=False))
