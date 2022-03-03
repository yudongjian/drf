from rest_framework.permissions import BasePermission


class IsHavePermission(BasePermission):
    # 判断是否有 视图的权限 return True/False
    def has_permission(self, request, view):
        print(request.user)
        print(type(request.user))
        if str(request.user) == "ydj":
            print("same")
            return True
        else:
            print("differ")
        return str(request.user) == "ydj"

    # 判断是否有 模型的权限
    def has_object_permission(self, request, view, obj):
            pass