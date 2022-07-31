from django.contrib import admin
from social.models import AccessRecord, Topic, Webpage, Users
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Users)

from social.models import UserProfileInfo
admin.site.register(UserProfileInfo)

from social.models import School, Student
admin.site.register(School)
admin.site.register(Student)

# admin.site.register
