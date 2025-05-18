from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Permission
from .serializers import PermissionSerializer


# Create your views here.
class PermissionViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer