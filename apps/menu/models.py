from django.db import models
from apps.permission.models import Permission

# Create your models here.
class Menu(models.Model):
    """菜单表"""
    name = models.CharField('菜单名称', max_length=32, unique=True)
    parent = models.ForeignKey('self', verbose_name='父菜单', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    order = models.IntegerField('菜单排序', default=0)
    path = models.CharField('菜单路径', max_length=128, null=True, blank=True)
    component = models.CharField('组件路径', max_length=128, null=True, blank=True)
    query = models.CharField('路由参数', max_length=128, null=True, blank=True)
    route_name = models.CharField('路由名称', max_length=128, null=True, blank=True)
    is_frame = models.BooleanField('是否内嵌', default=False)
    is_cache = models.BooleanField('是否缓存', default=False)
    icon = models.CharField('菜单图标', max_length=32, null=True, blank=True)
    is_hidden = models.BooleanField('是否隐藏', default=False)
    description = models.TextField('描述', null=True, blank=True)
    permissions = models.ManyToManyField(
        Permission,
        verbose_name='菜单权限',
        blank=True,
        related_name='menus',
        help_text='菜单关联的权限'
    )
    class Meta:
        ordering = ['order']
        verbose_name = '菜单'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
