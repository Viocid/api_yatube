from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated or request.method == permissions.SAFE_METHODS
            )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user 
