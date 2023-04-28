from rest_framework import permissions


class PermissionReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True

        if request.user.is_authenticated:
            return request.user.is_superuser or request.user.is_critic
