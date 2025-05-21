from django.db import models

# Create your models here.
class Permission(models.Model):
    """
    权限表（包含按钮级权限）
    type_choices = (
        ('api', '接口权限'),
        ('button', '按钮权限')
    )
    """
    type_choices = (
        ('api', '按钮权限'),
        ('menu', '菜单权限')
    )
    name = models.CharField('权限名称', max_length=32)
    codename = models.CharField('权限代码', max_length=128, unique=True)
    type = models.CharField('权限类型', max_length=8, choices=type_choices)
    method = models.CharField('请求方法', max_length=8, null=True, blank=True)  # 用于接口权限
    path = models.CharField('接口路径', max_length=128, null=True, blank=True)  # 用于接口权限
    description = models.TextField('描述', null=True, blank=True)

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}({self.codename})"