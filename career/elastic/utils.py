import json
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
        res = requests.get(req_url, headers=ES_HEADER)
        if res.status_code == 200:
            data = (res.content
                    .decode("utf-8"))
            return 0, data
        return 1, "获取索引列表失败"

    def index_create(self, index, alias, mappings):
        """创建索引

        Args:
            index: 索引名称
            alias: 索引别名
            mappings: 索引mapping

        Returns:

        """
        req_index_url = self.host + index
        index_data = json.dumps(mappings)

        req_alias_url = self.host + "_aliases"
        alias_data = {
            "actions": {
                "add": {
                    "index": index,
                    "alias": alias,
                }
            }
        }

        # NOTE: 创建索引
        res = requests.put(req_index_url,
                           headers=ES_HEADER,
                           data=index_data)
        if res.status_code == 200:
            # NOTE: 为索引指定别名
            res_alias = requests.post(req_alias_url,
                                      headers=ES_HEADER,
                                      data=json.dumps(alias_data))
            if res_alias.status_code == 200:
                return ""
            else:
                print("res:", res_alias.content.decode("utf-8"))
                return "索引创建成功，别名创建失败"
        else:
            print("res:", res.content.decode("utf-8"))
            return "索引创建失败"

    def index_rebuild(self, old_index, new_index, alias, mappings):
        """重建索引

        Args:
            old_index: 旧索引名称
            new_index: 新索引名称
            alias: 别名
            mappings: 索引mapping

        Returns:


        """
        msg = "索引重建失败: "

        # NOTE: 检查索引存在性
        status, data = self.index_list()
        if status == 0:
            if data.find(old_index) == -1:
                return msg + "旧索引不存在，请直接创建新索引"
            if data.find(new_index) > -1:
                return msg + "新索引已存在"
        else:
            return msg + "索引查询失败"

        # NOTE: 创建新索引
        create_index_url = self.host + new_index
        index_data = json.dumps(mappings)
        res_create = (requests.put(create_index_url,
                                   headers=ES_HEADER,
                                   data=json.dumps(index_data)))
        if res_create.status_code != 200:
            print("index create error:",
                  res_create.content.decode("utf-8"))
            return msg + "新索引创建失败"

        # NOTE: 迁移数据到新索引
        duplicate_data_url = self.host + "_reindex"
        duplicate_data = {
            "source": {
                "index": old_index
            },
            "dest": {
                "index": new_index
            }
        }
        res_reindex = requests.post(duplicate_data_url,
                                    headers=ES_HEADER,
                                    data=json.dumps(duplicate_data))
        if res_reindex.status_code != 200:
            print("reindex error:",
                  res_reindex.content.decode("utf-8"))
            return msg + "数据复制失败"

        # NOTE: 为新索引创建别名
        alias_url = self.host + "_aliases"
        alias_data = {
            "actions": [
                {
                    "remove": {
                        "alias": alias,
                        "index": old_index
                    }
                },
                {
                    "add": {
                        "alias": alias,
                        "index": new_index
                    }
                }
            ]
        }
        res_alias = (requests.post(alias_url,
                                   headers=ES_HEADER,
                                   data=json.dumps(alias_data)))
        if res_alias.status_code != 200:
            print("alias create error:",
                  res_alias.content.decode("utf-8"))
            return msg + "索引重命名失败"

        # 删除旧索引中的别名
        pass
