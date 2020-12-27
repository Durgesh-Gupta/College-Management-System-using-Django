from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# Create your models here
class BranchModel(models.Model):
    B_no=models.IntegerField()
    Bname=models.CharField(max_length=120)
    def __str__(s):
        return s.Bname


class Course(models.Model):
    Cname=models.CharField(max_length=120)
    img=models.ImageField(default="")
    clink=models.CharField(max_length=254)
    desc=models.CharField(max_length=150,default=None)
    branch=models.ForeignKey(BranchModel,on_delete=models.CASCADE)
    

    def __str__(s):
        return s.Cname
        
# # class Marks(models.Model):


class position(models.Model):
    position=models.CharField(max_length=30)
    def __str__(s):
        return s.position


class UserModel(User):
    # img=models.ImageField(default="")
    DOB=models.CharField(max_length=70)
    gender=models.CharField(max_length=10)
    contact=models.CharField(max_length=50)

    Branch=models.ForeignKey(BranchModel, on_delete=models.CASCADE)
    position=models.ForeignKey(position,on_delete=models.CASCADE,default=3)
    def __str__(s):
        return s.username

class Userform(UserCreationForm):
    class Meta:
        model=UserModel
        fields=['username','first_name','last_name','DOB','gender','contact','email','Branch','password1','password2']

 
# # Login--------------------------------------------->
class LoginForm(forms.Form):
    username=forms.CharField(max_length=40)
    password=forms.CharField(widget=forms.PasswordInput)

# #Emroll 



# # Staff Login

class Staff(User):
    conatct=models.CharField(max_length=50,default="")
    position=models.ForeignKey(position,on_delete=models.CASCADE,default=2)
    branch=models.ForeignKey(BranchModel,on_delete=models.CASCADE)
    createdDate=models.DateTimeField(auto_now_add=True)


class StaffForm(UserCreationForm):
    class Meta:
        model=Staff
        fields=['username','first_name','conatct','email','position','branch','password1','password2']
# Leave---------------------------------------------------
class leavestatus(models.Model):
    status=models.CharField(max_length=10)
    def __str__(s):
        return s.status

class Leave(models.Model):
    std_id=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    reason=models.CharField(max_length=120)
    message=models.TextField(max_length=420)
    status=models.ForeignKey(leavestatus,on_delete=models.CASCADE,default=1)

class Leaveform(forms.ModelForm):
    class Meta:
        model=Leave
        fields=['reason','message']

#         # image=models.ImageField(null=True,blank=True,upload_to="products")
#     # active=models.BooleanField(default=True)
#     # createdDate=models.DateTimeField(auto_now_add=True)
#     # updatedDate=models.DateTimeField(auto_now=True)