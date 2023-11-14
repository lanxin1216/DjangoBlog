import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, "db.sql"),
    }
}

REDIS_CONF = {
    "host": "127.0.0.1",
    "port": "6379"
}
REDIS_URL = f'redis://{REDIS_CONF["host"]}:{REDIS_CONF["port"]}'

DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 开发地址
SITE_URL = 'http://127.0.0.1:8000'

# 开发环境下邮件发送到控制台
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
