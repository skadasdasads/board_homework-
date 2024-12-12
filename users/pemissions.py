from rest_framework import permissions

class CustomReadOnly(permissions.Base.Permission):
    def jas_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author==request.user 