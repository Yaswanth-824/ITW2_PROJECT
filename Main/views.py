from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from project_ITW_sem3 import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from Main.models import *
from teacher.models import *
from teacher.views import is_teacher


def home(request):
    # news = News.objects.all()  'news' : news
    context = {
        'path' : '/',
        'users' : User.objects.filter(is_superuser = True)
    }
    if request.user.is_authenticated :
        if is_teacher(request.user) :
            context['path'] = '/teacher/'
        else :
            context['path'] = '/student/'
    return render(request,'home/school_website.html',context)

def gallery(request):
    return render(request,"home/gallery.html",{'path' : '/'})

def contact(request):
    return render(request,"home/contact.html",{'path' : '/'})

def about_us(request):
    return render(request,"home/about project.html",{'path' : '/'})

def forgot_password(request) :
    return render(request,"home/forgotpassword.html",{'path' : '/'})

def sign_out(request) :
    logout(request)
    return redirect('/')

def founder(request) :
    context = {
        'path' : '/',
        'users' : User.objects.filter(is_superuser = True)
    }
    return render(request,'home/founder.html',context)

def new_user(request):
    personal_info = forms.UserRegistrationForm()
    user = forms.user()
    data = {
        'path' : '/',
        'newUser' : personal_info,
        'user' : user,
        'class' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , "B.Tech" , "Degree"],
        'Subject' :['Telugu','Hindi','English','Maths','Science','Maths_a','Maths_b','Physics','Chemistry','Biology']
    }
    return render(request,"home/register.html",data)

def sign_in(request) :
    count = -1
    try :
        if request.method == "POST":
            uname = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = uname,password = password)
            if user is None :
                if User.objects.filter(username = uname) :
                    if User.objects.filter(username = uname ,password = password):
                        pass
                    else :
                        messages.error(request,"Plz veify your UserName/Paswword")
                        return redirect('/login/')
                elif User.objects.filter(password = password) :
                    if User.objects.filter(username = uname ,password = password):
                        pass
                    else :
                        messages.error(request,"Plz veify your UserName/Paswword")
                        return redirect('/login/')
                else :
                    messages.info(request,"Plz Register as new User ")
                    return redirect('/login/')
            else :
                profile = Profile.objects.get(user = user)
                if Teacher_Details.objects.filter(User_profileId = profile) :
                    login(request,user)
                    messages.info(request,"Logged in Sucessfully as a Teacher")
                    return redirect('/teacher/')
                elif Student_Details.objects.get(User_profileId = profile) :
                    login(request,user)
                    messages.info(request,"Logged in Sucessfully as a Student")
                    return redirect('/student/')
                else :
                    messages.info(request,"This User Not Registered as Teacher/Student")
                    return redirect('/login/')            
    except :
        pass
    return render(request,"home/login.html",{'path' : '/','Login_form' : forms.login(),'count' : count})
    
def register_user(request):
    if request.method == "POST":
        # Process the form data
        # form=forms.UserRegistrationForm(request.POST,request.FILES,instance=request.user.profile)
        first_name = request.POST.get('first_name')
        surname = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        photo = request.FILES.get('photo')
        if photo:
            # Create a unique file name for the photo
            fs = FileSystemStorage(location='media/user_photos/')
            Photo = fs.save(photo.name, photo)
            Photo = 'user_photos/'+ Photo
        country_code = request.POST.get('country_code')
        phone_number = request.POST.get('phone_number')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        Permanent_address = request.POST.get('Permanent_address')
        # check = User.objects.get(username = username)
        if 1 :
            if password == confirm_password :
                user = User.objects.create(
                    first_name = first_name,
                    last_name = surname,
                    username = username,
                    email = email,)
                password = user.set_password(password)
                user.save()
                profile = Profile(
                    user = user,
                    date_of_birth = date_of_birth,
                    gender = gender,
                    photo = Photo,
                    country_code = country_code,
                    phone_number = phone_number,
                    father_name = father_name,
                    mother_name = mother_name,
                    Permanent_address = Permanent_address,
                )
                profile.save()  # Save the user profile to the database
                # Determine the user's role (teacher or student) and create the corresponding object
                user_type = request.POST.get('user_type')
                if user_type == 'teacher':
                    User_profileId = profile
                    class_teacher = request.POST.get('class_Teacher')
                    subject = request.POST.get('subject')
                    salary = request.POST.get('salary')
                    date_of_enrollment = request.POST.get('dateofenrollment')
                    teacher = Teacher_Details(User_profileId = User_profileId , class_teacher=class_teacher, subject=subject, salary=salary,dateofenrollment = date_of_enrollment)
                    teacher.save()
                elif user_type == 'student':
                    User_profileId = profile
                    class_branch = request.POST.get('class_branch')
                    grade = request.POST.get('grade')
                    guardian_name = request.POST.get('Gardian_Name')
                    guardian_phone_number = request.POST.get('Gardian_Phone_Numbder')
                    father_phone_number = request.POST.get('Father_Phone_Numbder')  # Handle optional fields
                    mother_phone_number = request.POST.get('Mother_Phone_Numbder')  # Handle optional fields
                    student = Student_Details(User_profileId = User_profileId, class_branch=class_branch, grade=grade, guardian_name=guardian_name,
                                    guardian_phone_number=guardian_phone_number, father_phone_number=father_phone_number,
                                    mother_phone_number=mother_phone_number)
                    student.save()
                    attendence = Attendence_Data(student = student,status = 'P' )
                    attendence.save()
                messages.info(request,"Sucessfully Registered plz Login")
                return redirect('/login/')  # Redirect to the admin index page
            else :
                messages.info(request,"Plz Make Sure TO have Password,Conform-Password Same")
                return redirect('/new-user/')
        else :
            messages.info(request,"The User Name Already Take Plz Chooce a New One")
            return redirect('/new-user/')
    else :
        messages.info(request,"Plz register Your user Here")
    return redirect('/new-user/')



























            # if request.POST.get('role') == "teacher" :
            #     count = 0
            #     user = authenticate(username = uname,password = password)
            #     count = 1
            #     if user is None :
            #         messages.info(request,"Plz veify your UserName,Paswword")
            #         return redirect('/login/')
            #     else :
            #         profile = Profile.objects.get(user = user)
            #         role = Teacher_Details.objects.get(User_profileId = profile)
            #         if role is None :
            #             messages.info(request,"Incorrect Role Plz Select Correct Role")
            #             return redirect('/login/')
            #         else :
            #             login(request,user)
            #             messages.info(request,"Logged in Sucessfully as a Teacher")
            #             return redirect('/teacher/')
            # elif request.POST.get('role') == "student" :
            #     user = authenticate(username = uname,password = password )
            #     if user is None :
            #         messages.info(request,"Plz veify your UserName,Paswword")
            #     else :
            #         profile = Profile.objects.get(user = user)
            #         role = Student_Details.objects.get(User_profileId = profile)
            #         if role is None :
            #             messages.info(request,"Incorrect Role Plz Select Correct Role")
            #             return redirect('/login/')
            #         else :
            #             login(request,user)
            #             messages.info(request,"Logged in Sucessfully as a Teacher")
            #             return redirect('/student/')

