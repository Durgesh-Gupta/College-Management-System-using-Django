from django.contrib import admin
from .models import BranchModel,Course,position,leavestatus
# Register your models here.
class BranchAdmin(admin.ModelAdmin):
    class Meta:
        model=BranchModel
    

admin.site.register(BranchModel,BranchAdmin)


class CourseAdmin(admin.ModelAdmin):
    class Meta:
        model=Course
    

admin.site.register(Course,CourseAdmin)

# class EnrollAdmin(admin.ModelAdmin):
#     class Meta:
#         model=Enroll
    

# admin.site.register(Enroll,EnrollAdmin)
class PositionAdmin(admin.ModelAdmin):
    class Meta:
        model=position
    

admin.site.register(position,PositionAdmin)

class leaveadmit(admin.ModelAdmin):
    class Meta:
        model=leavestatus

admin.site.register(leavestatus,leaveadmit)