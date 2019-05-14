from django.db.models import QuerySet


class CreationQuerySet(QuerySet):

    def create_with_check(self, check, **kwargs):
        pass


class RetrieveQuerySet(QuerySet):

    def retrieve_with_field(self, **kwargs):
        pass


class UpdateQuerySet(QuerySet):
    pass


class DeletionQuerySet(QuerySet):
    pass


