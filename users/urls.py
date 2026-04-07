from django.urls import path
from .views import (
    user_register,
    user_login,
    token_refresh,
    user_logout,
    user_info,
    forgot_password
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
]
