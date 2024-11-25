from rest_framework.permissions import BasePermission 

class IsAuthenticatedUserOrReadOnly(BasePermission):
    def has_permission(self, request, view, obj):
        if request.method in ['GET', 'POST', 'PUT', 'DELETE']:
            return True
        