# @Author : WZ 
# @Time : 2019/5/14 11:35 
# @Intro : 开发配置

from .base import *

DEBUG = True

REDIS_OPTIONS = {}

ES_OPTIONS = {}

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # 'replica1': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'career',
    #     'HOST': 'dbreplica1',
    #     'TEST': {
    #         'MIRROR': 'default'
    #     }
    # }
}
