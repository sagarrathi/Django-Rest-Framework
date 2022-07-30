from rest_framework import permissions

from .permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    permission_classes=[permissions.IsAdminUser, IsStaffEditorPermission]


class UserQuerysetMixin():
    user_filed='user'

    """
    Why this works?
    """

    def get_queryset(self, *args, **kawrgs):
        lookup_data={}
        lookup_data[self.user_filed]=self.request.user
        print(lookup_data)
        qs=super().get_queryset(*args, **kawrgs)
        print("qs==>",qs)
        return qs.filter(**lookup_data)