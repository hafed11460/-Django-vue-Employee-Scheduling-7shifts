from rest_framework.permissions import BasePermission

class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_manager(): #or request.user.is_staff:
        # if request.user.is_authenticated:
            return True
        return False

    # def has_object_permission(self, request, view, obj):
    #     if obj.author == request.user:
    #         return True
    #     return False


class OwnerOrEmployeePermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.location.id == request.user.location.id:
            return True
        return False