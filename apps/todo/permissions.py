from rest_framework import permissions

class TodoPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.user.pk ==request.user.pk)