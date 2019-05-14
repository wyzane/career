from django.db.models import QuerySet

from core.querysets import (CreationQuerySet,
                            RetrieveQuerySet,
                            UpdateQuerySet,
                            DeletionQuerySet)


class ProjectQuerySet(CreationQuerySet,
                      RetrieveQuerySet,
                      UpdateQuerySet,
                      DeletionQuerySet,
                      QuerySet):
    pass