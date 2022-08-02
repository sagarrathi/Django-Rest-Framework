from rest_framework import permissions

from .permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    permission_classes=[permissions.IsAdminUser, IsStaffEditorPermission]


class UserQuerysetMixin():
    user_filed='user'
    allow_satff_view=False
    """
    Why this works?
    """

    def get_queryset(self, *args, **kawrgs):
        user=self.request.user
        lookup_data={}
        lookup_data[self.user_filed]=user
        # lookup_data={"owner":self.request.user}

        # print(lookup_data)
        qs=super().get_queryset(*args, **kawrgs)

        # give all data to staff as they can access admin
        if self.allow_satff_view and user.is_staff:
            return qs
        # print("qs==>",qs)

        return qs.filter(**lookup_data) # self.user_field=self.request.user