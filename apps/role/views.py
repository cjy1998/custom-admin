from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Role
from .serializers import RoleSerializer


# Create your views here.
class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer