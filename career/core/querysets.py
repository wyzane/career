from django.db.models import QuerySet


class CreationQuerySet(QuerySet):

    def create_with_check(self, check, **kwargs):
        pass


class RetrieveQuerySet(QuerySet):

    def existed(self, **kwargs):
        """过滤已删除数据
        """

        if hasattr(self.model, "is_deleted"):
            kwargs["is_deleted"] = False
        return super().filter(**kwargs)

    def retrieve_with_id(self, **kwargs):
        """根据id查询数据
        """
        if kwargs:
            info = super().filter(**kwargs)
        else:
            info = super().all()
        return info

    def retrieve_with_field(self, **kwargs):
        """根据条件查询数据
        """
        pass


class UpdateQuerySet(QuerySet):

    def update_by_id(self, id, **kwargs):
        objs = self.filter(id=id)
        if objs:
            objs.update(**kwargs)
        return objs


class DeletionQuerySet(QuerySet):

    def delete_by_id(self, id):
        obj = super().filter(id=id)
        if obj:
            obj.update(is_deleted=True)
            return obj.values(self.model.DISPLAY_FIELDS)[0]
        return {}



