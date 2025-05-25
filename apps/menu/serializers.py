from rest_framework import serializers

from apps.menu.models import Menu
from apps.permission.models import Permission


class BaseMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
class MenuSerializer(BaseMenuSerializer):
  pass
class MenuItemSerializer(BaseMenuSerializer):
    children = MenuSerializer(many=True)
    class Meta:
        model = Menu
        fields = '__all__'
    def create(self, validated_data):
        # permissions_data = validated_data.pop('permissions_data', [])
        children_data = validated_data.pop('children', [])
        # 创建菜单实例
        instance = super().create(validated_data)
        # # 处理权限（新增或关联已有）
        # permissions = []
        # for perm_data in permissions_data:
        #     # 通过codename查找或创建权限
        #     perm, _ = Permission.objects.get_or_create(
        #         codename=perm_data['codename'],
        #         defaults={
        #             'name': perm_data['name'],
        #             'type': perm_data['type'],
        #             'method': perm_data.get('method'),
        #             'path': perm_data.get('path'),
        #             'description': perm_data.get('description')
        #         }
        #     )
        #     permissions.append(perm)
        #
        # instance.permissions.set(permissions)
        # 批量创建子菜单（自动关联 parent_id）
        self.Meta.model.objects.bulk_create(
            [self.Meta.model(parent=instance, **child) for child in children_data]
        )
        return instance