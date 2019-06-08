from .base import *

DEBUG = True

REDIS_OPTIONS = {}

ES_OPTIONS = {}

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
SESSION_COOKIE_AGE = 300  # cookie有效时间
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # 是否关闭浏览器使得Session过期
SESSION_SAVE_EVERY_REQUEST = True
