import requests

from django.conf import settings

from .constants import ES_HEADER


class ESHandler:

    def __init__(self):
        self.host = ("http://{}:{}/"
                     .format(settings.ES_OPTIONS.get("HOST"),
                             settings.ES_OPTIONS.get("PORT")))

    def index_list(self):
        """获取elastic search索引列表

        Args:

        Returns:

        """
        req_url = self.host + "_cat/indices?v"
        print("url:", req_url)
        res = requests.get(req_url, headers=ES_HEADER)
        print("res:", res.content)
        return res.content
