from django.db import models
from django.contrib.auth.models import BaseUserManager

from core.managers import (BaseManager,
                           ExistedManager,
                           CRUDManager)


class UserManger(BaseManager,
                 ExistedManager,
                 CRUDManager,
                 BaseUserManager):
    def get_queryset(self):
        return (super()
                .get_queryset()
                .filter(is_deleted=False))
