from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from apps.permission.models import Permission
from apps.role.models import Role


# Create your models here.
class User(AbstractUser):
    """自定义用户模型"""
    roles = models.ManyToManyField(Role, verbose_name='拥有角色', blank=True,related_name='users')
    groups = models.ManyToManyField(
        Group,
        verbose_name='用户组',
        blank=True,
        help_text='用户所属的组，用于应用权限分组。',
        related_name="custom_user_set",  # 修改反向查询名称
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='用户权限',
        blank=True,
        help_text='用户拥有的特定权限。',
        related_name="custom_user_set",  # 修改反向查询名称
        related_query_name="custom_user",
    )
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    @property
    def button_permissions(self):
        """获取用户所有按钮权限码"""
        return self.get_all_permissions().filter(type='button').values_list('codename', flat=True)

    def get_all_permissions(self):
        """获取用户所有权限"""
        # print(self)
        # permissions = Permission.objects.none()
        # for role in self.roles.all():
        #     print(role.permissions.all())
        #     permissions |= role.permissions.all()
        # return permissions.distinct()
        print("aa",Permission.objects.filter(roles__users=self).distinct())
        return Permission.objects.filter(roles__users=self).distinct()
        # return Permission.objects.filter(roles__in=self.roles.all()).distinct()
        # return Permission.objects.filter(role__user=self).distinct()