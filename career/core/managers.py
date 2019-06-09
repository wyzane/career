from itertools import chain

from django.db import models


class BaseManager(models.Manager):

    def manager_only_method(self):
        return

    def display_fields(self, instance, fields):
        """模型显示指定字段
        """
        opts = instance._meta
        data = {}
        for f in chain(opts.concrete_fields,
                       opts.private_fields,
                       opts.many_to_many):
            if fields and f.name not in fields:
                continue
            data[f.name] = f.value_from_object(instance)
        return data


class ExistedManager(models.Manager):
    pass


class CRUDManager(models.Manager):

    def create_with_field_check(self, field_check, **kwargs):
        """创建对象

         Args:
            field_check: 检查条件字典

        Returns:
            obj: 创建成功的对象

        """
        print("-- create with check --")
        obj = self.filter(**field_check)
        if obj:
            obj = obj[0]
        else:
            obj = self.create(**kwargs)
        return obj

    def delete_with_field_check(self, field_check):
        """批量删除对象

        Args:
            field_check: 待删除对象的id列表

        Returns:
            objs: 删除成功的对象

        """
        print("-- delete with check --")
        if field_check:
            objs = self.filter(id__in=field_check)
        else:
            objs = self.all()

        if hasattr(self.model, "username"):
            for obj in objs:
                obj.username = obj.username + "_deleted"
                obj.is_deleted = True
            self.bulk_update(objs, ["username", "is_deleted"])
        elif hasattr(self.model, "name"):
            for obj in objs:
                obj.username = obj.username + "_deleted"
                obj.is_deleted = True
            self.bulk_update(objs, ["name", "is_deleted"])
        else:
            objs.update(is_deleted=True)
        return objs
