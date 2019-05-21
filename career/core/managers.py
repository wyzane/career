# @Author : WZ 
# @Time : 2019/5/21 14:48 
# @Intro :

from django.db import models


class BaseManager(models.Manager):

    def manager_only_method(self):
        return


class CRUDManager(models.Manager):
    pass


class RetrieveManager(models.Manager):
    pass