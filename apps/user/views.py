from pickle import FALSE

from django.contrib.auth import authenticate
from django.shortcuts import render
from drf_spectacular.utils import extend_schema

# Create your views here.
# views.py 新增部分
from rest_framework.decorators import action
from rest_framework import status, permissions
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer, UserLoginSerializer

'''
用户管理
'''

@extend_schema(tags=['用户管理'])
class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_serializer_context(self):
        """为序列化器添加当前用户上下文"""
        context = super().get_serializer_context()
        context['current_user'] = self.request.user
        return context

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        """修改密码专用接口"""
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'status': '密码已更新'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def me(self, request):
        """获取当前用户信息"""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    @action(detail=False,methods=['post'],permission_classes=[permissions.AllowAny])
    def login(self, request):
        """登录接口"""
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                user_data = UserLoginSerializer(user)
                return Response({
                    'token': str(refresh.access_token),
                    'refresh': str(refresh),
                    'userInfo': user_data.data
                })
            return Response({'error': '用户名或密码错误'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)