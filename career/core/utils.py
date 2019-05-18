

class Validator:
    """请求参数校验
    """

    def __init__(self, params):
        self.params = params
        self.err = ""
        self.msg = "参数错误，"

    def check(self, key, default="",
              valid_type=str, nullable=False):
        value = (self.params.get(key, default))

        if (not nullable) and (not value):
            self.err = (key + "为空")
        elif type(value) != valid_type:
            value = valid_type(value)

        if self.err:
            return False, self.err_msg(self.err)
        return value

    def err_msg(self, err):
        return self.msg + err


class RedisUtil:
    pass


class ESUtil:
    pass
