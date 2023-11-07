from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from . import forms
from django.contrib.auth import login, logout, authenticate
from Main.models import *
from django.contrib.auth.decorators import login_required



def home(request):
    # news = News.objects.all()  'news' : news
    return render(request,'home/school_website.html',{'path' : '/',})

def gallery(request):
    return render(request,"home/gallery.html",{'path' : '/'})

def contact(request):
    return render(request,"home/contact.html",{'path' : '/'})

def about_us(request):
    return render(request,"home/about project.html",{'path' : '/'})

def forgot_password(request) :
    return render(request,"home/forgotpassword.html",{'path' : '/'})

def new_user(request):
    newUser = forms.UserRegistrationForm()
    data = {
        'path' : '/',
        'newUser' : newUser,
        'class' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , "B.Tech" , "Degree"]
    }
    return render(request,"home/register.html",data)

def sign_in(request) :
    count = 0
    try :
        uname = request.POST.get('username')
        password = request.POST.get('password')
        if request.POST.get('role') == "teacher" :
            count = 1
            user = authenticate(username = uname,password = password)
            if user is None :
                messages.info(request,"Plz veify your UserName,Paswword")
            else :
                login(request,user)
                return redirect('/teacher/')
        elif request.POST.get('role') == "student" :
            user = authenticate(username = uname,password = password )
            if user is None :
                messages.info(request,"Plz veify your UserName,Paswword")
            else :
                login(request,user)
                return redirect('/student/')
    except :
        pass
    return render(request,"home/login.html",{'path' : '/','Login_form' : forms.login(),'count' : count})

def sign_out(request) :
    logout(request)
    return redirect('/')

def register_user(request):
    if request.method == "POST":
        # Process the form data
        # form=forms.UserRegistrationForm(request.POST,request.FILES,instance=request.user.profile)
        
        first_name = request.POST.get('first_name')
        surname = request.POST.get('surname')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        photo = request.POST.get('photo')
        country_code = request.POST.get('country_code')
        phone_number = request.POST.get('phone_number')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        Permanent_address = request.POST.get('Permanent_address')
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
            photo=photo,
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
            guardian_name = request.POST.get('guardian_name')
            guardian_phone_number = request.POST.get('guardian_phone_number')
            father_phone_number = request.POST.get('father_phone_number', '')  # Handle optional fields
            mother_phone_number = request.POST.get('mother_phone_number', '')  # Handle optional fields
            student = Student_Details(User_profileId = User_profileId, class_branch=class_branch, grade=grade, guardian_name=guardian_name,
                              guardian_phone_number=guardian_phone_number, father_phone_number=father_phone_number,
                              mother_phone_number=mother_phone_number)
            student.save()
        return redirect('/login/')  # Redirect to the admin index page
    return redirect('/new-user/')
# def Title_news(request,news_Title) :
#     about_title = News.objects.all()   
#     # get uses condition and also returns only onr row
#     # all get all rows Nwes.objects.get()
#     return render(request,'home/news.html',{'path' : '/','about_title' : about_title,'news_Title' : news_Title} )

# just a view is created to check the form
def form_check(request) :
    lp = forms.login()
    data = {'form' : lp}
    return render(request,'form_check.html',data)




# def teacher(request) :
#     count = 0
#     try :
#         if request.method =='POST' :
#             uname = request.POST.get('username')
#             password = request.POST.get('password')
#             count = 1
#             user = authenticate(username = uname,password = password)
#             if user is None :
#                 messages.info(request,"Plz veify your UserName,Paswword")
#             else :
#                 login(request,user)
#                 return redirect('/teacher/')
#     except :
#         pass
#     return render(request,"home/login.html",{'path' : '/','Login_form' : forms.login(),'count' : count})
# def student(request) :
#     count = 0
#     try :
#         if request.method =='POST' :
#             uname = request.POST.get('username')
#             password = request.POST.get('password')
#             count = 1
#             user = authenticate(username = uname,password = password)
#             if user is None :
#                 messages.info(request,"Plz veify your UserName,Paswword")
#             else :
#                 login(request,user)
#                 return redirect('/student/')
#     except :
#         pass