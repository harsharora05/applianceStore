from rest_framework import permissions 



class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check permissions for read-only request
        if request.method in permissions.SAFE_METHODS:
            return True
    
        # Check permissions for write request
        else:
            return bool(request.user and request.user.is_superuser)
               
   
