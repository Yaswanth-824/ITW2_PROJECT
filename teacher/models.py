from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import re
from Main.models import *
present = 0
# Create your models here.
class Attendence_Data(models.Model):
    student = models.ForeignKey(Student_Details,db_column='User ProfileId', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)  # Automatically set to today's date
    status_choices = (
        ('P', 'Present'),
        ('A', 'Absent'),
    )
    status = models.CharField(max_length=1, choices=status_choices,default='P',verbose_name = "Status")
    # total_classes = models.AutoField(primary_key=False)        
    def __str__(self):
        return str(self.student.User_profileId)
    def details(self):
        presents = Attendence_Data.objects.filter(student=self.student , status = 'Present').count()
        absents = Attendence_Data.objects.filter(student=self.student, status='Absent').count()
        if absents == None :
            absents = 0
        total_classes = presents + absents
        if total_classes > 0:
            percentage_attendance = (presents / total_classes) * 100
        else:
            percentage_attendance = 0
        return {
            'date' :self.date,
            'username': self.student.User_profileId,
            'total_classes' : total_classes,
            'No_Of_Presents' :presents,
            'percentage_attendance': percentage_attendance
        }
    
class Assignments(models.Model):
    title = models.CharField(max_length=100,null = True)
    teacher = models.ForeignKey(Teacher_Details,db_column='User TProfileId',on_delete=models.CASCADE)
    due_date = models.DateField(null = True)
    link_toupload = HTMLField(null = True)
    def __str__(self) :
        return str(self.teacher.User_profileId)
    def details(self) :
        return {
            'Title' : self.title,
            'DueDate' : self.due_date,
            'link' : self.link_toupload,
        }