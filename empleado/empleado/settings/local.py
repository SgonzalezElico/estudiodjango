#configuramos los atributos locales e importamos todo lo de base

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#hacemos una base de datos local  para no dañar la de produccion

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'sgonzalez',
        'PASSWORD': 'sgonzalez',
        'HOST': 'localhost',
        'PORT':'5432',
    }
}


STATIC_URL = 'static/'