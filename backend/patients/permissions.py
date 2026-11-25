from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrOwnPatient(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        if request.method in SAFE_METHODS:
            return obj.user_id == request.user.id

        return False