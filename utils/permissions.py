# permissions.py
from rest_framework import permissions
import re


class CustomPermission(permissions.BasePermission):
    """
    组合权限验证：
    1. 先验证接口权限（自动根据 path + method 匹配）
    2. 再验证视图声明的权限码
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            # 直接返回 False 触发 401 而不是 403
            # DRF 会自动处理认证失败响应
            return False
        # 超级管理员放行
        if request.user.is_superuser:
            return True

        # 第一步：验证接口权限
        current_path = request.path_info  # 获取标准化的路径（不带结尾斜杠）
        current_method = request.method

        # 获取用户所有 API 权限
        api_permissions = request.user.get_all_permissions().filter(type='api')
        print(request.user.get_all_permissions().values())
        # 检查是否匹配任意一个 API 权限规则
        for perm in api_permissions:
            # 路径正则匹配（示例：^/api/users/.*）
            path_match = re.fullmatch(perm.path, current_path) if perm.path else False
            # 方法匹配（支持 ALL 通配）
            method_match = (perm.method == 'ALL' or
                            current_method == perm.method)

            if path_match and method_match:
                return True

        # 第二步：验证视图声明的权限码
        # required_codenames = getattr(view, 'permission_codes', [])
        # if required_codenames:
        #     user_codenames = request.user.get_all_permissions().values_list('codename', flat=True)
        #     return any(code in user_codenames for code in required_codenames)

        # 默认拒绝
        return False