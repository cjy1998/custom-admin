from django.db import models

from apps.menu.models import Menu
from apps.permission.models import Permission


# Create your models here.
class Role(models.Model):
    """角色表"""
    name = models.CharField('角色名称', max_length=32, unique=True)
    permissions = models.ManyToManyField(Permission, verbose_name='拥有权限', blank=True, related_name='roles')
    menu = models.ManyToManyField(Menu, verbose_name='菜单', blank=True, related_name='roles')
    description = models.TextField('描述', null=True, blank=True)

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name