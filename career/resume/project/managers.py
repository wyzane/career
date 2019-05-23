# @Author : WZ 
# @Time : 2019/5/21 14:51 
# @Intro :

from django.db import models
from core.managers import (ExistedManager,
                           CRUDManager,
                           RetrieveManager)


class ProjectManager(ExistedManager,
                     CRUDManager,
                     RetrieveManager,
                     models.Manager):
    def get_queryset(self):
        """重写get_queryset()方法，过滤已删除数据
           调用all()等方法时，会自动过滤已删除数据
        """

        return (super()
                .get_queryset()
                .filter(is_deleted=False))
