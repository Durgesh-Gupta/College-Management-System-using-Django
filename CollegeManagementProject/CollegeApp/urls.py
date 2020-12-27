from django import urls
from django.urls import path
from . import views as v
urlpatterns = [
    path('',v.home),
    path('register',v.register),
    path('pregister',v.pregister),
    
    path('TEacherview',v.teacherview),

    path('slist',v.Studentlist.as_view()),
    path('clist',v.CourseList.as_view()),
    path('teacherlist',v.TeacherList.as_view()),

    path('editprofile/<int:id>',v.UpdateProfile),
    path('deletestud/<int:id>',v.deleteStudent),

    path('login',v.login_view),
    path('logout',v.logout_view),

    # path('enroll/<int:id>',v.EnrollCource),

    path('addStaff',v.addStaff),
    path('lf',v.leaveform),

]
