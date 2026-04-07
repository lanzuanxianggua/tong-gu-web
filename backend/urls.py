from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # API路由
    path('api/users/', include('users.urls')),
    path('api/detection/', include('detection.urls')),
    # 根路径返回前端index.html
    re_path(r'^$', TemplateView.as_view(template_name='index.html')),
    # 其他路径也返回index.html，支持前端路由
    re_path(r'^(?!api/|admin/|media/).*$', TemplateView.as_view(template_name='index.html')),
]

# 开发环境下提供媒体文件访问
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
