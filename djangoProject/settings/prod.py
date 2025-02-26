import os

from . import DEBUG
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "") != "False"
# DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "http://localhost:3000", ]

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

 #Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": int(os.environ["POSTGRES_DB_PORT"]),
    }
}

DROPBOX_OAUTH2_TOKEN = os.environ.get("DROPBOX_OAUTH2_TOKEN")
DROPBOX_ROOT_PATH = os.environ.get("DROPBOX_ROOT_PATH", "/cats_images/")