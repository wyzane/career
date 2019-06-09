from django.http.response import JsonResponse


class ResponseMixin:

    code_message = {
        "00000": "成功",
        "00001": "参数错误,",
        "00002": "对象不存在",
        "00003": "对象已存在",
        "00004": "创建错误，",
        "00005": "登录失败",
        "00006": "请重新登录",
    }

    def __init__(self):
        self._code = "00000"
        self._status = True
        self._message = "成功"

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, msg):
        self._message = msg
        # self._message = (self.code_message
        #                  .get(self.code) + msg)

    def get_json_response(self, data=None, **kwargs):
        res = dict()
        res["code"] = self.code
        res["status"] = self.status
        res["message"] = self.message
        res = {**res, **kwargs}
        res["data"] = data
        return JsonResponse(res)

