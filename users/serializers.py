from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import re
from .validators import validate_password_strength


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'first_name', 'last_name', 'date_joined', 'role']
        read_only_fields = ['id', 'date_joined']


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password', 'password_confirm']

    def validate_password(self, value):
        try:
            validate_password_strength(value)
        except ValueError as e:
            raise serializers.ValidationError(str(e))
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
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            phone=validated_data.get('phone'),
            password=validated_data['password']
        )
        return user


class LoginSerializer(TokenObtainPairSerializer):
    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        username_field = attrs.get('username', '')

        # 支持邮箱登录：如果输入包含 @，尝试查找对应用户名
        if '@' in username_field:
            try:
                user_obj = User.objects.get(email=username_field)
                attrs['username'] = user_obj.username
            except User.DoesNotExist:
                raise serializers.ValidationError('用户名或密码错误')

        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError('用户名或密码错误')
        if not user.is_active:
            raise serializers.ValidationError('账号已被禁用')
        data = super().validate(attrs)
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
    refresh = serializers.CharField()

    def validate(self, attrs):
        from rest_framework_simplejwt.tokens import RefreshToken
        from rest_framework_simplejwt.exceptions import TokenError
        try:
            refresh_token = RefreshToken(attrs['refresh'])
            access_token = str(refresh_token.access_token)
            return {'access': access_token, 'message': 'Token 刷新成功'}
        except TokenError as e:
            raise serializers.ValidationError(f'Token 无效或已过期：{str(e)}')


class ForgotPasswordSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True, error_messages={"required": "手机号码不能为空"})
    new_password = serializers.CharField(required=True, write_only=True, error_messages={"required": "新密码不能为空"})
    confirm_password = serializers.CharField(required=True, write_only=True, error_messages={"required": "请确认新密码"})
    captcha_key = serializers.CharField(required=True, error_messages={"required": "验证码标识不能为空"})
    captcha_code = serializers.CharField(required=True, error_messages={"required": "请输入验证码"})

    def validate_phone(self, value):
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('请输入正确的手机号码')
        return value

    def validate_new_password(self, value):
        try:
            validate_password_strength(value)
        except ValueError as e:
            raise serializers.ValidationError(str(e))
        return value

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'confirm_password': '两次输入的密码不一致'})
        try:
            user = User.objects.get(phone=attrs['phone'])
            if user.check_password(attrs['new_password']):
                raise serializers.ValidationError({'new_password': '新密码不能与旧密码相同'})
        except User.DoesNotExist:
            pass
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True, error_messages={"required": "请输入旧密码"})
    new_password = serializers.CharField(required=True, write_only=True, error_messages={"required": "新密码不能为空"})
    confirm_password = serializers.CharField(required=True, write_only=True, error_messages={"required": "请确认新密码"})

    def validate_old_password(self, value):
        request = self.context.get('request')
        if request and request.user:
            if not request.user.check_password(value):
                raise serializers.ValidationError('旧密码不正确')
        return value

    def validate_new_password(self, value):
        try:
            validate_password_strength(value)
        except ValueError as e:
            raise serializers.ValidationError(str(e))
        return value

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'confirm_password': '两次输入的密码不一致'})
        request = self.context.get('request')
        if request and request.user:
            if request.user.check_password(attrs['new_password']):
                raise serializers.ValidationError({'new_password': '新密码不能与旧密码相同'})
        return attrs
