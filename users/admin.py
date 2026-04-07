from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    自定义用户管理界面
    """
    # 在列表页面显示的字段
    list_display = ('username', 'email', 'phone', 'is_active', 'is_staff')
    # 添加搜索功能
    search_fields = ('username', 'email', 'phone')
    # 添加筛选功能
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    
    # 编辑页面的字段布局
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('个人信息', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('权限', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('重要日期', {'fields': ('last_login', 'date_joined')}),
    )
    
    # 添加用户时的字段布局
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'password1', 'password2'),
        }),
    )
