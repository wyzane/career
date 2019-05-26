from django.db import models

from core.managers import (ExistedManager,
                           CRUDManager,
                           RetrieveManager)


class HobbyManager(ExistedManager,
                   CRUDManager,
                   RetrieveManager,
                   models.Manager):
    def get_queryset(self):
        return (super()
                .get_queryset()
                .filter(is_deleted=False))
