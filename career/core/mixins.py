from django.http.response import JsonResponse


class ResponseMixin:

    code_message = {
        "00000": "成功",
        "00001": "参数错误,",
        "00002": "对象已存在",
        "00003": "对象不存在"
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
        return (self.code_message
                .get(self.code)
                + self._message)

    @message.setter
    def message(self, msg):
        self._message = msg

    def get_response(self, data=None, **kwargs):
        res = dict()
        res["code"] = self.code
        res["status"] = self.status
        res["message"] = self.message
        res["data"] = data
        res = {**res, **kwargs}
        return JsonResponse(res)

