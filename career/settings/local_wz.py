# @Author : WZ 
# @Time : 2019/5/21 11:37 
# @Intro :

from .dev import *

REDIS_OPTIONS = {
    "HOST": '192.168.0.101',
    "PORT": 6379,
    "password": "wyzane",
}

ES_OPTIONS = {
    "HOST": '192.168.0.103',
    "PORT": 9200,
    "NODE": ["192.168.0.104:9200"]
}

ES_HEADER = {"Content-Type": 'application/json'}

MAX_REDIS_CONNECTIONS = 10
