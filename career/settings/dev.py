from .base import *

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

DEBUG = True

REDIS_OPTIONS = {
    "HOST": '192.168.0.101',
    "PORT": 6379,
}

ES_OPTIONS = {
    "HOST": '192.168.0.103',
    "PORT": 9200,
    "NODE": ["192.168.0.104:9200"]
}

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'career',
        'USER': 'postgres',
        'PASSWORD': 'wyzane',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

# Session
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_COOKIE_AGE = 3600  # cookie有效时间
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # 是否关闭浏览器使得Session过期
SESSION_SAVE_EVERY_REQUEST = True

# Cron Config
JOB_STORE_URL = ("postgresql+psycopg2://{}:{}@{}:{}/{}".
                 format("postgres", "wyzane", "localhost",
                        "5432", "career"))
JOB_STORE = {
    'default': SQLAlchemyJobStore(url=JOB_STORE_URL)
}
EXECUTORS = {
    'default': ThreadPoolExecutor(5),
    'processpool': ProcessPoolExecutor(2)
}
JOB_DEFAULTS = {
    'coalesce': True,
    'max_instance': 2,

}
INTERVAL = 10
