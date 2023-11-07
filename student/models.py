from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import re
from Main.models import *

class Teache_subject_Class(models.Model):
    student = models.ForeignKey(Student_Details,db_column='User SProfileId', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher_Details,db_column='User TProfileId',on_delete=models.CASCADE)
    Subject = models.CharField(max_length=20,null= True)
    Class = models.CharField(max_length = 20,null = True)
    def __str__(self):
        return str(self.student)
    def teacher_info(self):
        return {
            'username' :self.student.User_profileId,
            'teacher' : self.teacher.User_profileId,
            'subject' :self.Subject,
        }

class primary_school(models.Model):
    student = models.ForeignKey(Student_Details,db_column='User ProfileId', on_delete=models.CASCADE)
    TELUGU = models.CharField(choices=[('Telugu','Yes'),('no','No')],max_length=10,null = False ,default='Yes')
    HINDI = models.CharField(choices=[('Hindi','Yes'),('no','No')],max_length=10,null = False ,default='Yes')
    ENGLISH = models.CharField(choices=[('English','Yes'),('no','No')],max_length=10,null = False ,default='Yes')
    MATHS = models.CharField(choices=[('Maths','Yes'),('no','No')],max_length=10,null = False ,default='Yes')
    SCIENCE = models.CharField(choices=[('Science','Yes'),('no','No')],max_length=10,null = False ,default='Yes')
    def __str__(self) :
        return str(self.student)
    def course_info(self) :
        return {
            'username' : self.student.User_profileId,
            'telugu' :self.TELUGU,
            'hindi' : self.HINDI,
            'english' : self.ENGLISH,
            'maths' : self.MATHS,
            'science' : self.SCIENCE,
        }
    
class high_school(models.Model):
    student = models.ForeignKey(Student_Details,db_column='User ProfileId', on_delete=models.CASCADE)
    TELUGU = models.CharField(choices=[('Telugu','Yes'),('no','No')],max_length=10,null = False ,default='Yes')
    HINDI = models.CharField(choices=[('Hindi','Yes'),('no','No')],max_length=10,null = False ,default='Yes')
    ENGLISH = models.CharField(choices=[('English','Yes'),('no','No')],max_length=10,null = False ,default='Yes')
    MATHS_A = models.CharField(choices=[('Maths_a','Yes'),('no','No')],max_length=10,null = False ,default='Yes')
    MATHS_B = models.CharField(choices=[('Maths_b','Yes'),('no','No')],max_length=10,null = False ,default='Yes')
    PHYSICS = models.CharField(choices=[('Physics','Yes'),('no','No')],max_length=10,null = False ,default='Yes')
    CHEMISTRY = models.CharField(choices=[('Chemistry','Yes'),('no','No')],max_length=10,null = False ,default='Yes')
    BIOLOGY = models.CharField(choices=[('Biology','Yes'),('no','No')],max_length=10,null = False ,default='Yes')
    def __str__(self) :
        return str(self.student)
    def course_info(self) :
        return {
            'username' : self.student.User_profileId,
            'telugu' :self.TELUGU,
            'hindi' : self.HINDI,
            'english' : self.ENGLISH,
            'maths_a' : self.MATHS_A,
            'maths_b' : self.MATHS_B,
            'physics' : self.PHYSICS,
            'chemistry' : self.CHEMISTRY,
            'biology' : self.BIOLOGY,
        }
    
class gradesheet(models.Model):
    gradechoices = [
        ('10','A'),
        ('9','B'),
        ('8','C'),
        ('7','D'),
        ('6','E'),
        ('5' ,'Fail'),
        ('0','Yes')
    ]
    student = models.ForeignKey(Student_Details,db_column='User ProfileId', on_delete=models.CASCADE)
    Subject = models.CharField(max_length=20,null= True)
    grade = models.CharField(choices=gradechoices,max_length=10,null = False ,default='Yes')
    def __str__(self) :
        return str(self.student.User_profileId)
    def grade_info(self) :
        return {
            'Subject' :self.Subject,
            'grade' : self.grade,
        }