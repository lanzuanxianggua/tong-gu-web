from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import re


class UserSerializer(serializers.ModelSerializer):
    """
    用户模型序列化器
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'first_name', 'last_name', 'date_joined', 'role']
        read_only_fields = ['id', 'date_joined']


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    用户注册序列化器 - 增强密码验证
    """
    password = serializers.CharField(
        write_only=True,
        required=True
        # 移除 Django 内置密码验证器，使用自定义验证逻辑
    )
    password_confirm = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password', 'password_confirm']
    
    def validate_password(self, value):
        """
        增强密码验证：
        1. 至少 8 个字符
        2. 包含大小写字母
        3. 包含数字
        4. 不能与用户名太相似
        """
        # 检查长度
        if len(value) < 8:
            raise serializers.ValidationError('密码长度至少为 8 位')
        
        # 检查是否包含大小写字母
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError('密码必须包含至少一个大写字母')
        
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError('密码必须包含至少一个小写字母')
        
        # 检查是否包含数字
        if not re.search(r'\d', value):
            raise serializers.ValidationError('密码必须包含至少一个数字')
        
        # 检查是否与用户名太相似
        if 'username' in self.initial_data:
            username = self.initial_data.get('username', '').lower()
            if username and (username in value.lower() or value.lower() in username):
                raise serializers.ValidationError('密码不能与用户名太相似')
        
        return value
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({'password_confirm': '两次输入的密码不一致'})
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({'username': '该用户名已被使用'})
        if attrs.get('phone') and User.objects.filter(phone=attrs['phone']).exists():
            raise serializers.ValidationError({'phone': '该手机号已被注册'})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        # create_user 会自动对密码进行加密存储
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            phone=validated_data.get('phone'),
            password=validated_data['password']
        )
        return user


class LoginSerializer(TokenObtainPairSerializer):
    """
    JWT 登录序列化器 - 继承自 TokenObtainPairSerializer
    返回 access token 和 refresh token
    """
    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    
    def validate(self, attrs):
        # 验证用户名密码
        user = authenticate(
            username=attrs['username'],
            password=attrs['password']
        )
        
        if not user:
            raise serializers.ValidationError('用户名或密码错误')
        
        # 检查用户是否激活
        if not user.is_active:
            raise serializers.ValidationError('账号已被禁用')
        
        # 调用父类方法获取 JWT token
        data = super().validate(attrs)
        
        # 添加额外信息
        data.update({
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'phone': user.phone,
                'role': user.role
            },
            'message': '登录成功'
        })
        
        return data


class TokenRefreshSerializer(serializers.Serializer):
    """
    刷新 Token 序列化器
    """
    refresh = serializers.CharField()
    
    def validate(self, attrs):
        from rest_framework_simplejwt.tokens import RefreshToken
        from rest_framework_simplejwt.exceptions import TokenError
        
        try:
            refresh_token = RefreshToken(attrs['refresh'])
            access_token = str(refresh_token.access_token)
            
            return {
                'access': access_token,
                'message': 'Token 刷新成功'
            }
        except TokenError as e:
            raise serializers.ValidationError(f'Token 无效或已过期：{str(e)}')


class ForgotPasswordSerializer(serializers.Serializer):
    """
    忘记密码序列化器
    """
    phone = serializers.CharField(required=True, error_messages={"required": "手机号码不能为空"})
    new_password = serializers.CharField(required=True, write_only=True, error_messages={"required": "新密码不能为空"})
    confirm_password = serializers.CharField(required=True, write_only=True, error_messages={"required": "请确认新密码"})
    
    def validate_phone(self, value):
        """
        验证手机号码
        """
        # 验证手机号码格式
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('请输入正确的手机号码')
        
        # 验证手机号码是否存在
        try:
            User.objects.get(phone=value)
        except User.DoesNotExist:
            raise serializers.ValidationError('该手机号码未注册')
        
        return value
    
    def validate_new_password(self, value):
        """
        验证新密码强度
        """
        # 检查长度
        if len(value) < 8:
            raise serializers.ValidationError('密码长度至少为 8 位')
        
        # 检查是否包含大小写字母
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError('密码必须包含至少一个大写字母')
        
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError('密码必须包含至少一个小写字母')
        
        # 检查是否包含数字
        if not re.search(r'\d', value):
            raise serializers.ValidationError('密码必须包含至少一个数字')
        
        return value
    
    def validate(self, attrs):
        """
        验证两次密码是否一致
        """
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'confirm_password': '两次输入的密码不一致'})
        
        # 验证新密码是否与旧密码相同
        try:
            user = User.objects.get(phone=attrs['phone'])
            if user.check_password(attrs['new_password']):
                raise serializers.ValidationError({'new_password': '新密码不能与旧密码相同'})
        except User.DoesNotExist:
            pass
        
        return attrs
