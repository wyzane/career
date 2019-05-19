from django.db.models import QuerySet


class CreationQuerySet(QuerySet):

    def create_with_check(self, check, **kwargs):
        pass


class RetrieveQuerySet(QuerySet):

    def existed(self):
        """过滤已删除数据
        """

        if hasattr(self.model, "is_deleted"):
            info = self.filter(is_deleted=False)
        else:
            info = self.all()
        return info

    def retrieve_with_id(self, id):
        """根据条件查询数据
        """

        info = self.filter(id=id)
        return info

    def retrieve_with_field(self, **kwargs):
        """根据条件查询数据
        """

        if kwargs:
            info = self.filter(**kwargs)
        else:
            info = self.all()
        print("info:", info)
        return info


class UpdateQuerySet(QuerySet):
    pass


class DeletionQuerySet(QuerySet):
    pass



