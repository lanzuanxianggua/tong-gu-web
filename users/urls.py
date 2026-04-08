from django.urls import path
from .views import (
    user_register,
    user_login,
    token_refresh,
    user_logout,
    user_info,
    forgot_password,
    user_profile,
    change_password
)

urlpatterns = [
    # 注册接口
    path('register/', user_register, name='user_register'),
    # 登录接口（JWT）
    path('login/', user_login, name='user_login'),
    # 刷新 Token 接口
    path('token/refresh/', token_refresh, name='token_refresh'),
    # 登出接口
    path('logout/', user_logout, name='user_logout'),
    # 获取用户信息
    path('info/', user_info, name='user_info'),
    # 忘记密码接口
    path('forgot-password/', forgot_password, name='forgot_password'),
    # 获取个人信息（需要登录）
    path('profile/', user_profile, name='user_profile'),
    # 修改密码（需要登录）
    path('change-password/', change_password, name='change_password'),
]
