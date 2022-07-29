from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        print("permission==>",user.get_all_permissions())
        if user.is_staff:
            # AppName.action_ModelName
            if user.has_perm("product.add_product"): 
                return True
            if user.has_perm("product.view_product"):
                return True
            if user.has_perm("product.change_product"):
                return True
            if user.has_perm("product.delete_product"):
                return True
        
            return False
        return False

    # def has_object_permission(self, request, view, obj):
    #     return obj.owner ==request.user
