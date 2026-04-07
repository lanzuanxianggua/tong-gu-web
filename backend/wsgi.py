import os

from django.core.wsgi import get_wsgi_application

# 设置 Django 的设置文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = get_wsgi_application()
