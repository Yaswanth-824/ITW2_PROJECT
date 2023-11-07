from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from Main.models import *
from teacher.models import *
from project_ITW_sem3.forms import *
from .models import *
from .forms import *
def is_student(user) :
    profile = Profile.objects.get(user = user)
    try:
        student = Student_Details.objects.get(User_profileId=profile)
    except Student_Details.DoesNotExist:
        student = None
    if student is None :
        return False
    else :
        return True

def is_registered(user) :
    profile = Profile.objects.get(user = user)
    student = Student_Details.objects.get(User_profileId=profile)
    try :
        primary_school.objects.get(student = student)
        return True
    except primary_school.DoesNotExist:
        try :
            high_school.objects.get(student = student)
            return True
        except high_school.DoesNotExist :
            return False


@login_required(login_url='/login/')     # For Logginin
@user_passes_test(is_student, login_url='/login/')  # To Check That User is in Correct Role or NOT
def home(request):
    context = {
        'path' : '/student/',
    }
    return render(request,'student/student.html',context)


@login_required(login_url='/login/')
@user_passes_test(is_student, login_url='/login/')
def profile(request):
    user = request.user
    profile = Profile.objects.get(user = user)
    deatil_profile = profile.user_profile_data()
    if profile is None :
        messages.info(request,"NOT Yet Registered ")
        return redirect('/logout/')
    else :
        studentdetails = Student_Details.objects.get(User_profileId = profile)
        if studentdetails is None :
            messages.info("You are Trying to Access Restricted Site")
            return redirect('/logout/')
        else :
            context = {
                'path' : '/student/',
                'profile' : deatil_profile,
                'student' : Student_Details.objects.get(User_profileId = profile).details(),
            }
        return render(request,'home/profile.html',context)

@login_required(login_url='/login/')
@user_passes_test(is_student, login_url='/login/')
@user_passes_test(is_registered, login_url='/student/register_course/')
def Gradesheet(request):
    context = {
        'path':'/student/',
    }
    user = request.user
    profile = Profile.objects.get(user = user)
    student = Student_Details.objects.get(User_profileId = profile)
    grade = gradesheet.objects.filter(student = student)
    grade_details = {}
    AVG_GRADE = 0
    j = 0
    for i in grade :
        grade_details[j] = i.grade_info()
        if i.grade == 'Yes' :
            AVG_GRADE += 0
        else :
            AVG_GRADE += int(i.grade)
        j = j + 1
    AVG_GRADE = AVG_GRADE/ j
    context['grade_info'] = grade_details
    context['avg_grade'] = AVG_GRADE
    return render(request,'student/gradesheet.html',context)

@login_required(login_url='/login/')
@user_passes_test(is_student, login_url='/login/')
@user_passes_test(is_registered, login_url='/student/register_course/')
def course_info(request):
    context = {
        'path' : '/student/'
    }
    try :
        user = request.user
        profile = Profile.objects.get(user = user)
        student = Student_Details.objects.get(User_profileId = profile)
        if student.class_branch in ['1','2','3','4','5'] :
            try :
                courses = primary_school.objects.get(student = student)
                register = Teache_subject_Class.objects.filter(student = student)
                info = {}
                j = 0
                for i in register :
                    info[j] = i.teacher_info()
                    j = j+1
                context = {
                   'path' : '/student/',
                   'courses' : courses.course_info(),
                   'register' : info
               }
            except primary_school.DoesNotExist :
                return redirect('/student/register_course/')
        else :
            try :
                courses = high_school.objects.get(student = student)
                register = Teache_subject_Class.objects.filter(student = student)
                info = {}
                j = 0
                for i in register :
                    info[j] = i.teacher_info()
                    j = j+1
                context = {
                    'path' : '/student/',
                    'courses' : courses.course_info(),
                    'register' : info ,
                }
            except high_school.DoesNotExist :
                return redirect('/student/register_course/')
    except :
        pass
    return render(request,'student/course_info.html',context)

@login_required(login_url='/login/')
@user_passes_test(is_student, login_url='/login/')
def register_course(request) :
    context = {
        'path' : '/student/'
    }
    user = request.user
    profile = Profile.objects.get(user = user)
    student = Student_Details.objects.get(User_profileId = profile)
    if student.class_branch in ['1','2','3','4','5'] :
        if request.method == "POST" :
            sub1 = request.POST.get('TELUGU')
            sub2 = request.POST.get('HINDI')
            sub3 = request.POST.get('ENGLISH')
            sub4 = request.POST.get('MATHS')
            sub5 = request.POST.get('SCIENCE')
            primary_school(student = student ,TELUGU = sub1 ,HINDI= sub2,ENGLISH = sub3,MATHS= sub4,SCIENCE = sub5 ).save()
            teach1 = request.POST.get('TELUGUteacher')
            user = User.objects.get(username = teach1)
            profile = Profile.objects.get(user = user)
            teach1 = Teacher_Details.objects.get(User_profileId = profile)
            teach2 = request.POST.get('HINDIteacher')
            user = User.objects.get(username = teach2)
            profile = Profile.objects.get(user = user)
            teach2 = Teacher_Details.objects.get(User_profileId = profile)
            teach3 = request.POST.get('ENGLISHteacher')
            user = User.objects.get(username = teach3)
            profile = Profile.objects.get(user = user)
            teach3 = Teacher_Details.objects.get(User_profileId = profile)
            teach4 = request.POST.get('MATHSteacher')
            user = User.objects.get(username = teach4)
            profile = Profile.objects.get(user = user)
            teach4 = Teacher_Details.objects.get(User_profileId = profile)
            teach5 = request.POST.get('SCIENCEteacher')
            user = User.objects.get(username = teach5)
            profile = Profile.objects.get(user = user)
            teach5 = Teacher_Details.objects.get(User_profileId = profile)
            Teache_subject_Class(student = student,teacher = teach1,Subject = sub1 ,Class = student.class_branch ).save()
            Teache_subject_Class(student = student,teacher = teach2,Subject = sub2 ,Class = student.class_branch ).save()
            Teache_subject_Class(student = student,teacher = teach3,Subject = sub3 ,Class = student.class_branch ).save()
            Teache_subject_Class(student = student,teacher = teach4,Subject = sub4 ,Class = student.class_branch ).save()
            Teache_subject_Class(student = student,teacher = teach5,Subject = sub5 ,Class = student.class_branch ).save()
            gradesheet(student = student,Subject = sub1,grade = '0').save()
            gradesheet(student = student,Subject = sub2,grade = '0').save()
            gradesheet(student = student,Subject = sub3,grade = '0').save()
            gradesheet(student = student,Subject = sub4,grade = '0').save()
            gradesheet(student = student,Subject = sub5,grade = '0').save()
            return redirect('/student/Courses_Info/')
        else :
            Subject = ['Telugu','Hindi','English','Maths','Science']
            context['form'] = primary_form()
            teachers = {}
            t = 0
            for i in Subject :
                teacher = Teacher_Details.objects.filter(subject = i)
                id = {}
                k=0
                for j in teacher :
                    id[k] = j
                    k = k+1
                teachers[i.upper()] = id
                t = t+1
            context['teacher'] = teachers
                
    else :
        if request.method == "POST" :
            sub1 = request.POST.get('TELUGU')
            sub2 = request.POST.get('HINDI')
            sub3 = request.POST.get('ENGLISH')
            sub4 = request.POST.get('MATHS_A')
            sub5 = request.POST.get('MATHS_B')
            sub6 = request.POST.get('PHYSICS')
            sub7 = request.POST.get('CHEMISTRY')
            sub8 = request.POST.get('BIOLOGY')
            high_school(student = student ,TELUGU = sub1 ,HINDI= sub2,ENGLISH = sub3,MATHS_A= sub4, MATHS_B= sub5 ,PHYSICS = sub6,CHEMISTRY = sub7,BIOLOGY = sub8).save()
            teach1 = request.POST.get('TELUGUteacher')
            user = User.objects.get(username = teach1)
            profile = Profile.objects.get(user = user)
            teach1 = Teacher_Details.objects.get(User_profileId = profile)
            teach2 = request.POST.get('HINDIteacher')
            user = User.objects.get(username = teach2)
            profile = Profile.objects.get(user = user)
            teach2 = Teacher_Details.objects.get(User_profileId = profile)
            teach3 = request.POST.get('ENGLISHteacher')
            user = User.objects.get(username = teach3)
            profile = Profile.objects.get(user = user)
            teach3 = Teacher_Details.objects.get(User_profileId = profile)
            teach4 = request.POST.get('MATHS Ateacher')
            user = User.objects.get(username = teach4)
            profile = Profile.objects.get(user = user)
            teach4 = Teacher_Details.objects.get(User_profileId = profile)
            teach5 = request.POST.get('MATHS Bteacher')
            user = User.objects.get(username = teach5)
            profile = Profile.objects.get(user = user)
            teach5 = Teacher_Details.objects.get(User_profileId = profile)
            teach6 = request.POST.get('PHYSICSteacher')
            user = User.objects.get(username = teach6)
            profile = Profile.objects.get(user = user)
            teach6 = Teacher_Details.objects.get(User_profileId = profile)
            teach7 = request.POST.get('CHEMISTRYteacher')
            user = User.objects.get(username = teach7)
            profile = Profile.objects.get(user = user)
            teach7 = Teacher_Details.objects.get(User_profileId = profile)
            teach8 = request.POST.get('BIOLOGYteacher')
            user = User.objects.get(username = teach8)
            profile = Profile.objects.get(user = user)
            teach8 = Teacher_Details.objects.get(User_profileId = profile)
            Teache_subject_Class(student = student,teacher = teach1,Subject = sub1 ,Class = student.class_branch ).save()
            Teache_subject_Class(student = student,teacher = teach2,Subject = sub2 ,Class = student.class_branch ).save()
            Teache_subject_Class(student = student,teacher = teach3,Subject = sub3 ,Class = student.class_branch ).save()
            Teache_subject_Class(student = student,teacher = teach4,Subject = sub4 ,Class = student.class_branch ).save()
            Teache_subject_Class(student = student,teacher = teach5,Subject = sub5 ,Class = student.class_branch ).save()
            Teache_subject_Class(student = student,teacher = teach6,Subject = sub6 ,Class = student.class_branch ).save()
            Teache_subject_Class(student = student,teacher = teach7,Subject = sub7 ,Class = student.class_branch ).save()
            Teache_subject_Class(student = student,teacher = teach8,Subject = sub8 ,Class = student.class_branch ).save()
            gradesheet(student = student,Subject = sub1).save()
            gradesheet(student = student,Subject = sub2).save()
            gradesheet(student = student,Subject = sub3).save()
            gradesheet(student = student,Subject = sub4).save()
            gradesheet(student = student,Subject = sub5).save()
            gradesheet(student = student,Subject = sub6).save()
            gradesheet(student = student,Subject = sub7).save()
            gradesheet(student = student,Subject = sub8).save()
            return redirect('/student/Courses_Info/')
        else :
            Subject = ['Telugu','Hindi','English','Maths_a','Maths_b','Physics','Chemistry','Biology']
            context['form'] = high_form()
            teachers = {}
            t = 0
            for i in Subject :
                teacher = Teacher_Details.objects.filter(subject = i)
                id = {}
                k=0
                for j in teacher :
                    id[k] = j
                    k = k+1
                if i == "Maths_a":
                    i = 'MATHS A'
                elif i == "Maths_b" :
                    i = 'MATHS B'
                teachers[i.upper()] = id
                t = t+1
            context['teacher'] = teachers
    return render(request,'student/register.html',context)

@login_required(login_url='/login/')
@user_passes_test(is_student, login_url='/login/')
@user_passes_test(is_registered, login_url='/student/register_course/')
def assignmentview(request):
    user = request.user
    user = User.objects.get(username = user)
    profile = Profile.objects.get(user = user)
    student = Student_Details.objects.get(User_profileId = profile)
    teacher_student = Teache_subject_Class.objects.filter(student = student)
    assignment_info = {}
    for i in teacher_student :
        try :
            k= 0
            assign = {}
            for j in Assignments.objects.filter(teacher = i.teacher) :
                assign[k] = j.details()
                k= k + 1
            assignment_info[i.Subject] = assign
        except Assignments.DoesNotExist :
            pass
    context = {
        'path' : '/student/',
        'info' : assignment_info,
    }
    return render(request,'student/assignment.html',context)

@login_required(login_url='/login/')
@user_passes_test(is_student, login_url='/login/')
def gallery(request):
    context = {
        'path' : '/student/',
    }
    return render(request,"home/gallery.html",context)


@login_required(login_url='/login/')
@user_passes_test(is_student, login_url='/login/')
def contact(request):
    context = {
        'path' : '/student/',
    }
    return render(request,"home/contact.html",context)

@login_required(login_url='/login/')
@user_passes_test(is_student, login_url='/login/')
def about_us(request):
    context = {
        'path' : '/student/'
    }
    return render(request,"home/about project.html",context)

@login_required(login_url='/login/')
@user_passes_test(is_student, login_url='/login/')
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
        return redirect('/student/profile/')
    context = {'data' : profile.user_profile_data(),'path' : '/student/'}
    return render(request,'home/updateprofile.html',context)
