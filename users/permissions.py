from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        if request.user.is_superuser is True:
            return obj
        else:
            return obj.id == request.user.id
