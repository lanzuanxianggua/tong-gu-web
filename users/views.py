from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from backend.utils import error_response
from .serializers import (
    UserSerializer,
    UserRegisterSerializer,
    LoginSerializer,
    TokenRefreshSerializer,
    ForgotPasswordSerializer,
    ChangePasswordSerializer
)
from .models import User
import logging
import io
import secrets
import string
from django.core.cache import cache

logger = logging.getLogger(__name__)


@api_view(['POST'])
@permission_classes([AllowAny])
def user_register(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'message': '注册成功',
            'user': UserSerializer(user).data,
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=status.HTTP_201_CREATED)
    return error_response('注册失败', serializer.errors)


@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    return error_response('登录失败', serializer.errors, status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([AllowAny])
def token_refresh(request):
    serializer = TokenRefreshSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    return error_response('Token 刷新失败', serializer.errors, status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    try:
        refresh_token = request.data.get('refresh')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': '登出成功'}, status=status.HTTP_200_OK)
        return error_response('请提供 refresh token')
    except Exception as e:
        return error_response(f'登出失败：{str(e)}')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    return Response({
        'user': UserSerializer(request.user).data,
        'message': '获取成功'
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def generate_captcha(request):
    """生成图形验证码"""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return error_response('验证码服务不可用', status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    code = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    captcha_key = secrets.token_urlsafe(32)

    cache.set(f'captcha:{captcha_key}', code, timeout=120)

    width, height = 160, 40
    img = Image.new('RGB', (width, height), (42, 34, 28))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 28)
    except Exception:
        font = ImageFont.load_default()

    for i, ch in enumerate(code):
        x = 8 + i * 24
        y = secrets.randbelow(8)
        color = (secrets.randbelow(41) + 180, secrets.randbelow(41) + 160, secrets.randbelow(51) + 30)
        draw.text((x, y), ch, fill=color, font=font)

    for _ in range(4):
        x1, y1 = secrets.randbelow(width), secrets.randbelow(height)
        x2, y2 = secrets.randbelow(width), secrets.randbelow(height)
        draw.line((x1, y1, x2, y2), fill=(80, 70, 60), width=1)

    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    import base64
    captcha_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return Response({
        'captcha_key': captcha_key,
        'captcha_image': f'data:image/png;base64,{captcha_image}'
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def forgot_password(request):
    captcha_key = request.data.get('captcha_key', '')
    captcha_code = request.data.get('captcha_code', '')

    if captcha_key and captcha_code:
        cached_code = cache.get(f'captcha:{captcha_key}')
        cache.delete(f'captcha:{captcha_key}')
        if not cached_code:
            return error_response('验证码已过期，请重新获取')
        if cached_code.upper() != captcha_code.upper():
            return error_response('验证码错误')
    else:
        return error_response('请提供验证码')

    serializer = ForgotPasswordSerializer(data=request.data)
    if serializer.is_valid():
        phone = serializer.validated_data['phone']
        new_password = serializer.validated_data['new_password']
        try:
            user = User.objects.get(phone=phone)
            user.set_password(new_password)
            user.save()
        except User.DoesNotExist:
            pass
        return Response({'message': '如果该手机号已注册，密码已重置成功'}, status=status.HTTP_200_OK)
    return error_response('请求数据无效', serializer.errors)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        new_password = serializer.validated_data['new_password']
        try:
            request.user.set_password(new_password)
            request.user.save()
            return Response({'message': '密码修改成功'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f'Change password failed: {e}')
            return error_response('密码修改失败，请稍后重试', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return error_response('请求数据无效', serializer.errors)
