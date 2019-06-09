from django.contrib.auth.backends import ModelBackend

from account.user.models import UserInfo


class LoginBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        """用户登录认证

        Args:
            username: 用户名
            password: 密码

        Returns:

        """
        try:
            user = (UserInfo.objects
                    .get(username=username,
                         password=password))
            return user
        except UserInfo.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = (UserInfo.objects
                    .get(pk=user_id))
            return user
        except UserInfo.DoesNotExost:
            return None