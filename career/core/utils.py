

class Validator:
    """请求参数校验
    """

    def __init__(self, params):
        self.params = params
        self.detail = ""

    def arg_check(self, arg_key, default="",
              arg_type=str, nullable=True):
        """请求参数校验

        Args:
            arg_key: 参数名
            default: 参数默认值
            arg_type: 参数类型
            nullable: 是否可以为空

        Returns:

        """
        value = self.params.get(arg_key, default)
        if (not nullable) and (not value):
            self.detail += (arg_key + "为空")
        if value:
            try:
                value = arg_type(value)
            except ValueError:
                self.detail += (arg_key + "类型错误")

        return value

    def arg_msg(self):
        if not self.detail:
            return True, ""
        return False, self.detail


class RedisUtil:
    pass


class ESUtil:
    pass
