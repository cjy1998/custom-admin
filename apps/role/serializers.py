from rest_framework import serializers

from apps.menu.models import Menu
from apps.menu.serializers import MenuSerializer
from apps.permission.models import Permission
from apps.permission.serializers import PermissionSerializer
from apps.role.models import Role


class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)
    menus = MenuSerializer(many=True, read_only=True)
    menu_ids = serializers.PrimaryKeyRelatedField(
        queryset=Menu.objects.all(),
        source='menus',
        many=True,
        write_only=True
    )
    permission_ids = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(),
        source='permissions',
        many=True,
        write_only=True
    )

    class Meta:
        model = Role
        fields = ['id', 'name', 'description', 'permissions', 'permission_ids', 'menus', 'menu_ids']