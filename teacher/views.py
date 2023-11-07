from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from Main.models import *
from .models import *
from student.forms import *
from student.models import *
from project_ITW_sem3.forms import *
from .forms import *
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView
from django.http import HttpResponse,HttpResponseRedirect
import datetime
#
# Decorator To ChecK Whter user is Teacher or Not
def is_teacher(user) :
    profile = Profile.objects.get(user = user)
    try:
        teacher = Teacher_Details.objects.get(User_profileId=profile)
    except Teacher_Details.DoesNotExist:
        teacher = None
    if teacher is None :
        return False
    else :
        return True



@login_required(login_url = '/login/')
@user_passes_test(is_teacher, login_url='/login/')
def home(request):
    username = request.user.username
    # return render(request,'teacher/teacher.html',{'path' : '/teacher/','data': messages.get_messages(request)})
    return render(request,'teacher/teacher.html',{'path' : '/teacher/'})


@login_required(login_url = '/login/')
@user_passes_test(is_teacher, login_url='/login/')
def profile(request):
    user = request.user
    profile = Profile.objects.get(user = user)
    deatil_profile = profile.user_profile_data()
    if profile is None :
        messages.info(request,"NOT Yet Registered as Teacher")
        return redirect('/logout/')
    else :
        teacherdetails = Teacher_Details.objects.get(User_profileId = profile)
        if teacherdetails is None :
            messages.info("You are Trying to Access Restricted Site")
            return redirect('/logout/')
        else :
            context = {
                'path' : '/teacher/',
                'profile' : deatil_profile,
                'details' : teacherdetails,
                'teacher' : Teacher_Details.objects.get(User_profileId = profile).details()
            }
        return render(request,'home/profile.html',context)


@login_required(login_url = '/login/')
@user_passes_test(is_teacher, login_url='/login/')
def Attendence(request):
    context = {
            'path' : '/teacher/',
            'class' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , "B.Tech" , "Degree"]
        }
    if request.method == "GET" :
        Class = request.GET.get('Class')
        student = Student_Details.objects.filter(class_branch = Class)
        user = request.user
        profile = Profile.objects.get(user = user)
        teacher = Teacher_Details.objects.get(User_profileId = profile)
        j = 0
        dstudent = {}
        for i in student :
            attendence = Attendence_Data.objects.filter(student = i).first()
            if Teache_subject_Class.objects.filter(student = i , teacher = teacher) :
                dstudent[j] = attendence.details()
                j = j+1
        context['dstudent'] = dstudent
        context['Class'] = Class
        url = f'/teacher/update/?Class={Class}'
        context['url'] = url
        context['date'] = datetime.date.today()
        return render(request,'teacher/Attendence.html',context)
    return render(request,"teacher/Attendence.html",context)

@login_required(login_url = '/login/')
@user_passes_test(is_teacher, login_url='/login/')
def StudentsDetails(request):
    slist = {}
    user1 = request.user
    profile = Profile.objects.get(user = user1)
    TGrade = Teacher_Details.objects.get(User_profileId = profile)
    students = Teache_subject_Class.objects.filter(teacher = TGrade)
    # Tgrade = TGrade.class_teacher
    # student = Student_Details.objects.filter(class_branch = Tgrade)
    o = 0
    for i in students :
        user = User.objects.get(username = i)
        profile = Profile.objects.get(user = user)
        j = Student_Details.objects.get(User_profileId = profile)
        sprofile = j.student_details()
        slist[o] = sprofile
        o = o+1
    context ={
        'path' : '/teacher/',
        'slist' : slist,
        'o' : o,
    }
    return render(request,'teacher/StudentsDetails.html',context)

@login_required(login_url = '/login/')
@user_passes_test(is_teacher, login_url='/login/')
def update(request) :
    if request.method == "POST" :
        username = request.POST.get('username')
        user = User.objects.get(username = username)
        profile = Profile.objects.get(user = user)
        student = Student_Details.objects.get(User_profileId = profile)
        Class = student.class_branch
        Attendence_Data(student =student,status = request.POST.get('status') ).save()
        url = f'/teacher/Attendence/?Class={Class}'
        return redirect(url)

@login_required(login_url = '/login/')
@user_passes_test(is_teacher, login_url='/login/')
def gradeupdate(request):
    user = request.user
    profile = Profile.objects.get(user = user)
    teacher = Teacher_Details.objects.get(User_profileId = profile)
    students = Teache_subject_Class.objects.filter(teacher = teacher)
    context = {
        'path' : '/teacher/'
    }
    if request.method == "POST" :
        student  = request.POST.get('username')
        user = User.objects.get(username = student)
        profile = Profile.objects.get(user = user)
        student = Student_Details.objects.get(User_profileId = profile)
        Grade = gradesheet.objects.get(student = student,Subject = teacher.subject)
        form = GradeUpdateForm(request.POST, instance = Grade)
        if form.is_valid():
            form.save()
            return redirect('/teacher/gradeupdate/')
    student = {}
    j= 0
    if not students  :
        return render(request,'teacher/gradesheetupdate.html',context)
    else :
        for i in students :
            student[j] = {'student' : i, 'subject' : i.Subject }
            j = j+1
        context = {
            'path' : '/teacher/',
            'students' : student ,
            'form' : GradeUpdateForm()
        }
        return render(request,'teacher/gradesheetupdate.html',context)

@login_required(login_url = '/login/')
@user_passes_test(is_teacher, login_url='/login/')
def assignment(request) :
    user  = request.user
    profile = Profile.objects.get(user = user)
    teacher = Teacher_Details.objects.get(User_profileId = profile)
    Assisient_info = Assignments.objects.filter(teacher = teacher)
    assignment_info = {}
    j = 0
    for i in Assisient_info :
        assignment_info[j] = i.details()
        j= j+1
    if request.method == "POST" :
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        link = request.POST.get('link_toupload')
        Assignments(title = title,teacher= teacher,due_date= due_date,link_toupload = link).save()
        return redirect('/teacher/assignment/')
    context ={
        'path' : '/teacher/',
        'form' : assignment_form(),
        'info' : assignment_info,
    }
    return render(request,'teacher/assignment.html',context)

@login_required(login_url = '/login/')
@user_passes_test(is_teacher, login_url='/login/')
def deleteAssignment(request) :
    if request.method == "POST" :
        title = request.POST.get('title')
        assignment = Assignments.objects.filter(title = title)
        for i in assignment :
            i.delete()
        return redirect('/teacher/assignment')
# common For Every Page
@login_required(login_url = '/login/')
@user_passes_test(is_teacher, login_url='/login/')
def updateprofile(request) :
    user = request.user
    user = User.objects.get(username= user)
    profile = Profile.objects.get(user = user)
    if request.method == "POST" :
        first_name = request.POST.get('first_name')
        surname = request.POST.get('last_name')
        email = request.POST.get('email')
        User.objects.filter(username = user).update(first_name = first_name,last_name = surname,email= email)
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        photo = request.FILES.get('photo')
        phone_number = request.POST.get('phone_number')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        Permanent_address = request.POST.get('Permanent_address')
        Profile.objects.filter(user = user).update(date_of_birth=date_of_birth,gender= gender,phone_number= phone_number,father_name = father_name,mother_name = mother_name,Permanent_address= Permanent_address)
        if request.FILES.get('photo') :
            if photo:
            # Create a unique file name for the photo
                fs = FileSystemStorage(location='media/user_photos/')
                Photo = fs.save(photo.name, photo)
            Photo = 'user_photos/'+ Photo
            Profile.objects.filter(user = user).update(photo = Photo)
        return redirect('/teacher/profile/')
    context = {'data' : profile.user_profile_data(),'path' : '/teacher/'}
    return render(request,'home/updateprofile.html',context)

@login_required(login_url = '/login/')
@user_passes_test(is_teacher, login_url='/login/')
def updateduedate(request) :
    user  = request.user
    profile = Profile.objects.get(user = user)
    teacher = Teacher_Details.objects.get(User_profileId = profile)
    if request.method == "POST" :
        title = request.POST.get('title')
        Assignments.objects.filter(teacher = teacher,title = title).update(due_date= request.POST.get('due_date'))
        return redirect('/teacher/assignment/')
def gallery(request):
    return render(request,"home/gallery.html",{'path' : '/teacher/'})

def contact(request):
    return render(request,"home/contact.html",{'path' : '/teacher/'})

def about_us(request):
    return render(request,"home/about project.html",{'path' : '/teacher/'})

# Create your views here.

