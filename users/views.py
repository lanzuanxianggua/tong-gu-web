from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
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

logger = logging.getLogger(__name__)


@api_view(['POST'])
@permission_classes([AllowAny])
def user_register(request):
    """
    普通用户注册接口
    密码会自动加密存储
    """
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        
        # 生成 JWT token
        refresh = RefreshToken.for_user(user)
        
        return Response(
            {
                'message': '注册成功',
                'user': UserSerializer(user).data,
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            },
            status=status.HTTP_201_CREATED
        )
    return Response(
        {
            'message': '注册失败',
            'errors': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    """
    普通用户登录接口 - JWT 认证
    返回 access token 和 refresh token
    """
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        # serializer 已经包含 JWT token 和用户信息
        return Response(
            serializer.validated_data,
            status=status.HTTP_200_OK
        )
    return Response(
        {
            'message': '登录失败',
            'errors': serializer.errors
        },
        status=status.HTTP_401_UNAUTHORIZED
    )


@api_view(['POST'])
@permission_classes([AllowAny])
def token_refresh(request):
    """
    刷新 Token 接口
    使用 refresh token 获取新的 access token
    """
    serializer = TokenRefreshSerializer(data=request.data)
    if serializer.is_valid():
        return Response(
            serializer.validated_data,
            status=status.HTTP_200_OK
        )
    return Response(
        {
            'message': 'Token 刷新失败',
            'errors': serializer.errors
        },
        status=status.HTTP_401_UNAUTHORIZED
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    """
    用户登出接口
    将 refresh token 加入黑名单（可选）
    """
    try:
        # 获取客户端传来的 refresh token
        refresh_token = request.data.get('refresh')
        
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response(
                {'message': '登出成功'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'message': '请提供 refresh token'},
                status=status.HTTP_400_BAD_REQUEST
            )
    except Exception as e:
        return Response(
            {'message': f'登出失败：{str(e)}'},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    """
    获取当前用户信息
    需要 JWT token 认证
    """
    user = request.user
    return Response(
        {
            'user': UserSerializer(user).data,
            'message': '获取成功'
        },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
@permission_classes([AllowAny])
def forgot_password(request):
    """
    忘记密码接口
    通过手机号码修改密码
    """
    serializer = ForgotPasswordSerializer(data=request.data)
    if serializer.is_valid():
        phone = serializer.validated_data['phone']
        new_password = serializer.validated_data['new_password']
        
        try:
            # 查找用户
            user = User.objects.get(phone=phone)
            
            # 更新密码
            user.set_password(new_password)
            user.save()
            
            return Response(
                {
                    'message': '密码修改成功'
                },
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {
                    'message': '该手机号码未注册'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {
                    'message': f'密码修改失败：{str(e)}'
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    return Response(
        {
            'message': '请求数据无效',
            'errors': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """
    获取当前用户个人信息
    需要 JWT token 认证
    """
    user = request.user
    return Response(
        {
            'user': UserSerializer(user).data,
            'message': '获取成功'
        },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    """
    修改密码接口
    需要登录，验证手机号码后修改密码
    """
    serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        phone = serializer.validated_data['phone']
        new_password = serializer.validated_data['new_password']
        
        try:
            # 验证手机号码是否匹配当前用户
            if request.user.phone != phone:
                return Response(
                    {
                        'message': '手机号码与当前用户不匹配'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # 更新密码
            request.user.set_password(new_password)
            request.user.save()
            
            return Response(
                {
                    'message': '密码修改成功'
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    'message': f'密码修改失败：{str(e)}'
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    return Response(
        {
            'message': '请求数据无效',
            'errors': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )
