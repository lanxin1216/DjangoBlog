from django.conf import settings

# 邮件配置
EMAIL_HOST = "你的邮件服务器HOST"
EMAIL_PORT = 25 if settings.DEBUG else 465
EMAIL_HOST_TLS = True if settings.DEBUG else False
EMAIL_USE_SSL = False if settings.DEBUG else True
EMAIL_HOST_USER = "用户名"
EMAIL_HOST_PASSWORD = "密码"
EMAIL_FROM = "你的邮件地址"
DEFAULT_FROM_EMAIL = '用户收到邮件显示的邮箱'
