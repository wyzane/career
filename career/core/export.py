"""从数据库导出数据
"""

from import_export import resources

from account.user.models import UserInfo


class ResourceUser(resources.ModelResource):
    class Meta:
        model = UserInfo
