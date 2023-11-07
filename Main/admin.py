from django.contrib import admin
from .models import *

# Register your models here.
class newsAdmin(admin.ModelAdmin) :
    list_display = ('title','image','content','title_slug')
admin.site.register(News,newsAdmin)

class ProfileAdmin(admin.ModelAdmin) :
    list_display = ('user','date_of_birth',)
admin.site.register(Profile,ProfileAdmin)

class TeacherAdmin(admin.ModelAdmin) :
    list_display = ( 'User_profileId',)
admin.site.register(Teacher_Details,TeacherAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('User_profileId','student_id',)
admin.site.register(Student_Details,StudentAdmin)
