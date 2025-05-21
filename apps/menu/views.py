from django.shortcuts import render
from django.views import View
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from apps.menu.models import Menu
from apps.menu.serializers import MenuSerializer, MenuItemSerializer


# Create your views here.
@extend_schema(tags=['菜单管理'])
class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer