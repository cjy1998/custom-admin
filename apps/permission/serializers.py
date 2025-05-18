from rest_framework import serializers

from apps.permission.models import Permission


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename', 'type', 'method', 'path', 'description']