from django.shortcuts import render

# Create your views here.
# views.py 新增部分
from rest_framework.decorators import action
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer


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