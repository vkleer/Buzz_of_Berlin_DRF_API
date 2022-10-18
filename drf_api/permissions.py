from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    A class for the IsOwnerOrReadOnly custom permission
    """
    def has_object_permission(self, request, view, obj):
        """
        Checks if the logged in user is the owner of the object
        and if so, give full access to the object.
        If the logged in user is not the owner of the object,
        give read-only access to the object.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
