from django.urls import path
from .views import (
    user_register,
    user_login,
    token_refresh,
    user_logout,
    user_info,
    forgot_password,
    generate_captcha,
    change_password
)

urlpatterns = [
    path('register/', user_register, name='user_register'),
    path('login/', user_login, name='user_login'),
    path('token/refresh/', token_refresh, name='token_refresh'),
    path('logout/', user_logout, name='user_logout'),
    path('info/', user_info, name='user_info'),
    path('captcha/', generate_captcha, name='generate_captcha'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('change-password/', change_password, name='change_password'),
]
