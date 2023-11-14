from celery import Celery
import os
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
app = Celery('myblog')
app.now = timezone.now
# 命名空间 namespace='CELERY'定义所有与celery相关的配置的键名要以'CELERY_'为前缀。
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
