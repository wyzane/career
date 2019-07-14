from .base import *

DEBUG = True

REDIS_OPTIONS = {}

ES_OPTIONS = {
    "HOST": '192.168.0.104',
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
