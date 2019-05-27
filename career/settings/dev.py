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
