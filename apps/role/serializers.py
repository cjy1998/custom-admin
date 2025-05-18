from rest_framework import serializers

from apps.permission.models import Permission
from apps.permission.serializers import PermissionSerializer
from apps.role.models import Role


class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)
    permission_ids = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(),
        source='permissions',
        many=True,
        write_only=True
    )

    class Meta:
        model = Role
        fields = ['id', 'name', 'description', 'permissions', 'permission_ids']