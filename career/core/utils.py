import json


class Validator:
    """请求参数校验
    """

    SPECIAL_TYPE = ['json', 'list']

    def __init__(self, params):
        self.params = params
        self.detail = ""
        self.arg_null = []
        self.arg_type = []

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
            self.arg_null.append(arg_key)
        elif value and (arg_type not in self.SPECIAL_TYPE):
            try:
                value = arg_type(value)
            except ValueError:
                self.arg_type.append(arg_key)
        elif arg_type in self.SPECIAL_TYPE:
            value = json.loads(value)

        return value

    def arg_msg(self):
        if self.arg_null:
            self.detail = ("参数" + self.arg_null[0] + "为空"
                           if len(self.arg_null) == 1
                           else "参数" + ",".join(self.arg_null) + "为空")
        if self.arg_type:
            self.detail = ("参数" + self.arg_type[0] + "类型错误"
                           if len(self.arg_type) == 1
                           else "参数" + ",".join(self.arg_type) + "类型错误")

        if not self.detail:
            return True, ""
        return False, self.detail


class RedisUtil:
    pass


class ESUtil:
    pass


class PGUtil:
    pass


class CrontabUtil:
    pass
