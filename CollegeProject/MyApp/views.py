from django.shortcuts import render,HttpResponse,redirect
from .models import Userform,UserModel,Course,LoginForm,position,Staff,StaffForm,User
from django.contrib.auth.models import User

from django.views.generic import ListView,UpdateView
# Create your views here.
def home(request):
    return render(request,'home.html')

def pregister(request):
    return render(request,'pre-register.html')

def register(request):
    if request.method=='POST':
        f=Userform(request.POST)
        f.save()
        return redirect('/')
    else:
        f=Userform
        return render(request,'registerpage.html',{'forms':f})

# lists------------------------------>
class Studentlist(ListView):
    model=UserModel

    template_name="studentlist.html"
    # teacdep=
    # stlist=UserModel.objects.filter()


class CourseList(ListView):
    model=Course
    template_name="course.html"

class TeacherList(ListView):
    model=Staff
    template_name="stafflist.html"

# Logi------------------->
from django.contrib.auth import login,logout,authenticate

def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('usern')
        passw=request.POST.get('passw')
        # print(uname)
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session['uid']=user.id
            login(request,user)

            

            return redirect('/')



        else:
            msg="Invalid username or password"
            return render(request,'form.html',{'msg':msg})
    else:
        lf=LoginForm
        return render(request,'form.html',{'forms':lf})
            
def logout_view(request):
    logout(request)
    return redirect('/')

# logout end ----------------------->>>>>


# STaff Login
def addStaff(request):
    if request.method=='POST':
        f=StaffForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=StaffForm
        return render(request,'registerpage.html',{'forms':f})


# Update Profile

def UpdateProfile(request,id):
    e=UserModel.objects.get(id=id)
    if request.method=='POST':
        st=Userform(request.POST,instance=e)
        st.save()
        return redirect('/')
    else:
        st=Userform(instance=e)
    return render(request,'registerpage.html',{'forms':st})

def deleteStudent(request,id):
    st=UserModel.objects.get(id=id)
    st.delete()
    return redirect('/')




def teacherview(request):
    sid=request.session.get('uid')
    print(sid)
    staff=Staff.objects.filter(id=sid)
    print(staff)
    # for i in staff:
    #     print(i.branch)
    bid=staff[0].branch
    totalstudent=UserModel.objects.filter(Branch=bid).count()
    # print(totalstudent)
    d={'totalstudent':totalstudent}

    return render(request,'thome.html',d)