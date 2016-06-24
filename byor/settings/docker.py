from base import *
from os import environ


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'byordb',
        'USER': 'root',
        'PASSWORD': environ.get('DB_ENV_MYSQL_ROOT_PASSWORD'),
        'HOST': environ.get('DB_PORT_3306_TCP_ADDR'),
        'PORT': environ.get('DB_PORT_3306_TCP_PORT'),
    }
}
