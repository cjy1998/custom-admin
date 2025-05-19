# serializers.py 新增部分
from rest_framework import serializers
from .models import User
from ..role.models import Role
from ..role.serializers import RoleSerializer


class UserSerializer(serializers.ModelSerializer):
    # 只写字段（用于创建/更新）
    password = serializers.CharField(
        write_only=True,
        required=False,
        style={'input_type': 'password'}
    )
    role_ids = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),
        source='roles',  # 关联到模型的 roles 字段
        many=True,
        write_only=True,
        required=False
    )

    # 只读字段（用于展示）
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email',
            'is_active', 'date_joined',
            'password', 'roles', 'role_ids'
        ]
        extra_kwargs = {
            'email': {'required': True}
        }

    def create(self, validated_data):
        """创建用户时处理密码"""
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        """更新用户时选择性更新密码"""
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)
class UserLoginSerializer(serializers.Serializer):
        username = serializers.CharField(required=True)
        password = serializers.CharField(required=True, write_only=True)
        roles = RoleSerializer(many=True, read_only=True)
        class Meta:
            model = User
            fields = ['username', 'password', 'token', 'roles', 'permissions']
