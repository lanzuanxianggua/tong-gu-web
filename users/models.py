from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    自定义用户模型
    """
    # 用户角色选项
    ROLE_CHOICES = (
        ('admin', '系统管理员'),
        ('user', '普通用户'),
    )
    
    phone = models.CharField(
        max_length=11,
        unique=True,
        verbose_name='手机号',
        blank=True,
        null=True,
        help_text='用户手机号，用于验证码登录'
    )
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='user',
        verbose_name='用户角色',
        help_text='用户角色，默认为普通用户，系统管理员拥有所有权限'
    )
    
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
    
    def __str__(self):
        return self.username
