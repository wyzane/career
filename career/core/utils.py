import json
import redis
import requests

from apscheduler.schedulers.background import BackgroundScheduler

from django.conf import settings


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
            self.detail = ("参数错误，" + self.arg_null[0] + "为空"
                           if len(self.arg_null) == 1
                           else "参数" + ",".join(self.arg_null) + "为空")
        if self.arg_type:
            self.detail = ("参数错误，" + self.arg_type[0] + "类型错误"
                           if len(self.arg_type) == 1
                           else "参数" + ",".join(self.arg_type) + "类型错误")

        if not self.detail:
            return True, ""
        return False, self.detail


class RedisUtil:

    pool = redis.ConnectionPool(host=settings.REDIS_OPTIONS.get("HOST"),
                                port=settings.REDIS_OPTIONS.get("PORT"),
                                password=settings.REDIS_OPTIONS.get("password"),
                                max_connections=settings.MAX_REDIS_CONNECTIONS)

    instance = redis.Redis(connection_pool=pool)

    def set(self, data, ex=None, op=None):
        """保存字符串数据

        Args:
            op: 是否批量操作

        Returns:

        """
        if not data:
            return False

        result = None

        if not op:
            key = list(data.keys())[0]
            val = data.get(key)
            result = self.instance.set(key, val, ex)
        elif op == "m":
            result = self.instance.mset(**data, ex=ex)
        return result

    def get(self, key, op=None):
        """获取字符串数据
        """
        if not key:
            return False

        results = []
        bytes_val = []

        if not op:
            tmp_val = self.instance.get(key)
            bytes_val.append(tmp_val)
        elif op == "m":
            bytes_val = self.instance.mget(*key)
        else:
            return None

        if not bytes_val:
            return None

        try:
            for val in bytes_val:
                result = val.decode("utf-8")
                results.append(result)
        except AttributeError:
            return None
        return results

    def get_set(self, key, val):
        """获取旧值，同时更新值
        """
        if not key:
            return False

        result = None
        val = self.instance.getset(key, val)
        try:
            result = val.decode("utf-8")
        except AttributeError:
            pass
        return result

    def set_json(self, key, val, ex=None):
        """写入json数据
        """
        result = self.instance.set(key, val, ex)
        return result

    def get_json(self, key):
        """写入json数据
        """
        result = None
        val = self.instance.get(key)
        try:
            tmp_ret = val.decode("utf-8")
            result = json.loads(tmp_ret)
        except (AttributeError, TypeError):
            pass
        return result


class ESUtil:

    session = requests.Session()

    def __init__(self):
        self.session.headers = settings.ES_HEADER

    def query(self, index, cons):
        """查询接口

        Args:
            index: 索引
            cons: 查询条件

        Returns:

        """
        pass


class PGUtil:
    pass


class CronUtil:

    scheduler = BackgroundScheduler(jobstores=settings.JOB_STORE,
                                    job_defaults=settings.JOB_DEFAULTS)

    @staticmethod
    def cron_task(func):
        job = CronUtil.scheduler.add_job(func,
                                         "interval",
                                         seconds=settings.INTERVAL)
        CronUtil.scheduler.start()
        return job
