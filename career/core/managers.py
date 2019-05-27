from django.db import models


class BaseManager(models.Manager):

    def manager_only_method(self):
        return


class ExistedManager(models.Manager):

    def get_queryset(self):
        return (super(ExistedManager, self)
                .get_queryset()
                .filter(is_deleted=False))


class CRUDManager(models.Manager):
    pass
