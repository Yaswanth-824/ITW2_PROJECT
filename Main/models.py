# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField    
from autoslug  import AutoSlugField      # pip install django-autoslug
from django.core.exceptions import ValidationError
from datetime import date
import re

# Create your models here.
class News(models.Model) :
    title = models.CharField(max_length=25)
    image = models.FileField(upload_to='news/',default = None)
    content = HTMLField()
    title_slug = AutoSlugField(populate_from = 'title' ,unique=True)
    # AutoSlugField(populate_from = "" ,unique = True) 
    def __str__(self) :
        return self.title

    
class Profile(models.Model) :
    COUNTRY_CODE_CHOICES = [
        ('+91', 'India (+91)'),
        ('+1', 'United States (+1)'),
        # Add more country code choices as needed
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField(verbose_name='Date of Birth',null=True)
    gender = models.CharField(
        max_length=10,
        choices=[('none', 'Select Gender'), ('male', 'Male'), ('female', 'Female'), ('trans', 'Other')],
        verbose_name='Gender'
    )
    photo = models.FileField(upload_to='user_photos/',max_length = 100, verbose_name='Photo')
    country_code = models.CharField(
        max_length=5,
        choices=COUNTRY_CODE_CHOICES,
        verbose_name='Country Code'
    )
    phone_number = models.CharField(max_length=15, verbose_name='Phone Number')
    father_name = models.CharField(max_length=100, verbose_name='Father Name')
    mother_name = models.CharField(max_length=100, verbose_name='Mother Name')
    Permanent_address = models.CharField(max_length=255, verbose_name='Permanent Address')
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
        ordering = ["-date_of_birth"]
    def __str__(self):
        return self.user.username
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age
    def user_profile_data(self):
        data = {
            'first_name': self.user.first_name,
            'surname': self.user.last_name,
            'date_of_birth': self.date_of_birth,
            'gender': self.gender,
            'photo': self.photo.url,
            'country_code': self.country_code,
            'phone_number': self.phone_number,
            'father_name': self.father_name,
            'mother_name': self.mother_name,
            'username': self.user.username,
            'email': self.user.email,
            'Permanent_address': self.Permanent_address,
            'age': self.age(),
        }
        return data

# or we can create Teacher(UserProfile) :
# ctreate a feild for foreign key
class Teacher_Details(models.Model):
    User_profileId = models.ForeignKey(Profile, on_delete=models.CASCADE)
    teacher_id = models.AutoField(primary_key=True)
    class_teacher = models.CharField(max_length=100, verbose_name='Class Teacher', default = "B.tech" ,null=True)
    subject = models.CharField(max_length=100, verbose_name='Subject',null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salary',null=True)
    dateofenrollment = models.DateTimeField(verbose_name='date of enrollment',null=True)  # Field name made lowercas
    class Meta:
        verbose_name = "Teacher_Details"
        verbose_name_plural = "Teacher_Detailss"
        ordering = ["-teacher_id"]
    def __str__(self):
        return str(self.User_profileId)
    def details(self):
        return {
            'class_teacher' :self.class_teacher,
            'subject' : self.subject
        }

class Student_Details(models.Model):
    User_profileId = models.ForeignKey(Profile, on_delete=models.CASCADE,verbose_name="User profileId")
    student_id = models.AutoField(primary_key=True)
    class_branch = models.CharField(max_length=100, verbose_name='Class/Branch',null=True)
    grade = models.CharField(max_length=10, verbose_name='Grade',null=True)
    guardian_name = models.CharField(max_length=100, verbose_name='Guardian Name',null=True)
    guardian_phone_number = models.CharField(max_length=15, verbose_name='Guardian Phone Number',null=True)
    father_phone_number = models.CharField(max_length=15, verbose_name='Father Phone Number', blank=True, null=True)
    mother_phone_number = models.CharField(max_length=15, verbose_name='Mother Phone Number', blank=True, null=True)
    
    def __str__(self):
        return  str(self.User_profileId)
    def details(self):
        return {
            'class_branch' : self.class_branch,
            'grade' : self.grade,
        }
    def student_details(self):
        User_profileId = self.User_profileId
        user = User.objects.get(username = User_profileId)
        # Retrieve all profiles and their associated student details
        profiles_with_student_details = Profile.objects.get(user = user).user_profile_data()
        data_list ={}
        # Convert the data into a list of dictionaries
        student_data = {
                'userName' :User_profileId,
                'class_branch':self.class_branch,
                'grade':self.grade,
                'guardian_name':self.guardian_name,
                'guardian_phone_number':self.guardian_phone_number,
                'father_phone_number':self.father_phone_number,
                'mother_phone_number':self.mother_phone_number,
            }
        data_list = {'profile': profiles_with_student_details, 'student_details': student_data}
        return data_list

# class Login(models.Model) :
#     ROLES = [
#         ('teacher', 'Teacher'),
#         ('student', 'Student'),
#     ]
#     username = models.CharField(max_length=10, verbose_name='Username', unique=True)
#     password = models.CharField(
#         max_length=8,
#         verbose_name='Password',
#         help_text='Password must contain at least one lowercase letter, one capital letter, and one number.',
#     )
#     role = models.CharField(
#         max_length=10,
#         choices=ROLES,
#         verbose_name='Role',
#         default='None'
#     )
#     def validate_password(self):
#         if not re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$', self.password):
#             raise ValidationError('Password must contain at least one lowercase letter, one capital letter, and one number.')

#     def save(self):
#         self.validate_password()
#         super().save()
    
#     def __str__(self):
#         return {'username': self.username, 'role': self.role}

