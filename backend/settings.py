from pathlib import Path

# 获取项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent


# 密钥配置
import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

from django.core.exceptions import ImproperlyConfigured


def _get_env(name, default=None, required=False):
    value = os.environ.get(name, default)
    if required and not value:
        raise ImproperlyConfigured(f"环境变量 {name} 未设置，请在 .env 文件中配置")
    return value

# 使用环境变量中的密钥（必须在 .env 中配置）
SECRET_KEY = _get_env('SECRET_KEY', required=True)

# 控制 Django 的调试模式（默认关闭，生产环境安全）
DEBUG = _get_env('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',') if os.environ.get('ALLOWED_HOSTS') else []

# 生产环境安全设置
if not DEBUG:
    # 告诉 Django 信任反向代理的 HTTPS 头
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


# 安装的应用
INSTALLED_APPS = [
    "django.contrib.admin",  # 管理员界面
    "django.contrib.auth",   # 认证系统
    "django.contrib.contenttypes",  # 内容类型系统
    "django.contrib.sessions",  # 会话系统
    "django.contrib.messages",  # 消息系统
    "django.contrib.staticfiles",  # 静态文件系统
    # CORS 支持
    "corsheaders",  # 跨域请求头处理
    # 自定义应用
    "users",
    "detection",
    "rest_framework",  # 用于构建 RESTful API
    "rest_framework.authtoken", # 用于 API 身份验证
    "rest_framework_simplejwt.token_blacklist",  # JWT token 黑名单（登出功能）
]

MIDDLEWARE = [
    # 跨域请求头处理中间件 - 必须放在最前面
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI 协议 ：WSGI 是 Python Web 应用和 Web 服务器之间的标准接口，定义了两者之间的通信规范
# WSGI 应用入口
WSGI_APPLICATION = "backend.wsgi.application"


# 数据库配置
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get('DB_NAME', 'tong-gu'),
        "USER": os.environ.get('DB_USER', 'root'),
        "PASSWORD": _get_env('DB_PASSWORD', required=True),
        "HOST": os.environ.get('DB_HOST', '127.0.0.1'),
        "PORT": os.environ.get('DB_PORT', '3306'),
        "OPTIONS": {
            "charset": "utf8mb4",
        }
    }
}



# 密码验证器
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# 语言和时区配置
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# 静态文件配置
STATIC_URL = "static/"
STATICFILES_DIRS = []
STATIC_ROOT = BASE_DIR / 'static'

# 媒体文件配置
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# 默认主键类型
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 自定义用户模型
AUTH_USER_MODEL = 'users.User'

# REST Framework 配置
REST_FRAMEWORK = {
    # 默认权限方案 - 需要认证
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    # 默认认证类 - 同时支持 JWT 和 Token 认证
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    # 默认渲染器
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    # 速率限制
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/minute',
        'user': '30/minute',
    }
}

# Simple JWT 配置
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
}

# 文件上传大小限制 - 50MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50 * 1024 * 1024
FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50 * 1024 * 1024


# CORS 配置
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
    "http://localhost:3003",
    "http://localhost:3004",
    "http://localhost:8080",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
    "http://127.0.0.1:3002",
    "http://127.0.0.1:3003",
    "http://127.0.0.1:3004",
    "http://127.0.0.1:8080",
    "https://tong-gu.cn",
    "https://www.tong-gu.cn",
    "http://tong-gu.cn",
    "http://www.tong-gu.cn",
    "https://api.tong-gu.cn",
    "http://api.tong-gu.cn",
]

# 允许的HTTP方法
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

# 允许的请求头
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

# 允许携带凭证（如cookies）
CORS_ALLOW_CREDENTIALS = True

# 日志配置
LOG_DIR = BASE_DIR / 'logs'
LOG_DIR.mkdir(exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(LOG_DIR / 'django.log'),
            'maxBytes': 1024*1024*100,  # 100MB
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}
