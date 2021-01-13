from rest_framework import permissions

class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.user_type == "user"

class IsUserCreate_IsNurseryList(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method == "POST" and request.user.user_type == "user":
            return True
        elif request.method == "GET" and request.user.user_type == "nursery":
            return True
        return False

class IsNurseryCreate_IsUserList(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method == "POST" and request.user.user_type == "nursery":
            return True
        elif request.method == "GET" and request.user.user_type == "user":
            return True
        return False