from django import urls
from django.urls import path
from . import views as v
urlpatterns = [
    path('',v.home),
    path('register',v.register),
    path('pregister',v.pregister),
    path('about',v.About),
    path('contact',v.Contact),
    
    path('TEacherview',v.teacherview),

    path('slist',v.Studentlist.as_view()),
    path('clist',v.CourseList.as_view()),
    path('teacherlist',v.TeacherList.as_view()),

    path('editprofile/<int:id>',v.UpdateProfile),
    path('editmarks/<int:id>',v.UpdateMarks),
    path('deletestud/<int:id>',v.deleteStudent),
    
    path('appreje/<int:id>',v.appreje),

    path('login',v.login_view),
    path('logout',v.logout_view),

    # path('enroll/<int:id>',v.EnrollCource),

    path('addStaff',v.addStaff),
    
    path('lf',v.leaveform),
    path('appleav/<int:id>',v.LeaveSelect),
    path('appleav',v.leavlist),

    path('addMarks',v.addMarks),
    path('MarksList',v.MarksList),
    path('SMarksList',v.SMarksList),

    path('MyCourse',v.MyCourse),

]
