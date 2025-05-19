from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from .models import Permission
from .serializers import PermissionSerializer


# Create your views here.
@extend_schema(tags=['权限管理'])

class PermissionViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer