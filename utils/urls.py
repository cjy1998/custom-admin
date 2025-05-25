from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.permission.views import PermissionViewSet
from apps.role.views import RoleViewSet
from apps.user.views import UserViewSet
from apps.menu.views import MenuViewSet
router = DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet,)  # 新增用户路由
router.register(r'permissions', PermissionViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'menus', MenuViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('current-user/permissions/', CurrentUserPermissions.as_view()),
    path('auth/', include('rest_framework.urls')),  # 保留登录登出
]