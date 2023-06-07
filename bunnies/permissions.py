from rest_framework import permissions


class RabbitHolePermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return super().has_permission(request, view)
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return super().has_object_permission(request, view, obj)
        # returns true if the user is the owner of the rabbit hole
        print("called", request.user)
        return request.user == obj.owner

