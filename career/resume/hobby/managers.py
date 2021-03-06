from django.db import models

from core.managers import (ExistedManager,
                           CRUDManager)


class HobbyManager(ExistedManager,
                   CRUDManager,
                   models.Manager):
    def get_queryset(self):
        return (super()
                .get_queryset()
                .filter(is_deleted=False))
