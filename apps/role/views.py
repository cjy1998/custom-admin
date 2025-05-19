from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from .models import Role
from .serializers import RoleSerializer


# Create your views here.
@extend_schema(tags=['角色管理'])

class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer