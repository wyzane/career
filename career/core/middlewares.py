from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from core.mixins import ResponseMixin


class LoginMiddleware(MiddlewareMixin,
                      ResponseMixin):

    def process_request(self, request):
        req_path = request.path
        if req_path not in settings.EXCLUDE_PATH:
            username = request.session.get("username")
            user_id = request.session.get("user_id")
            if (not username) or (not user_id):
                self.code = "00006"
                self.status = False
                self.message = "请重新登录"
                return self.get_json_response()


# class LoginMiddleware(ResponseMixin):
#
#     def __init__(self, get_response=None):
#         self.get_response = get_response
#         super().__init__()
#
#     def __call__(self, request):
#         req_path = request.path
#         if req_path not in settings.EXCLUDE_PATH:
#             username = request.session.get("username")
#             user_id = request.session.get("user_id")
#             if (not username) or (not user_id):
#                 self.code = "00006"
#                 self.status = False
#                 self.message = "请重新登录"
#                 return self.get_json_response()
#             return self.get_json_response
