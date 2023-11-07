from django.contrib import admin
from .models import *
# Register your models here.

class Teache_subject_ClassAdmin(admin.ModelAdmin) :
    link_display = ('student','teacher','Subject')

class primary_schoolAdmin(admin.ModelAdmin) :
    link_display = ('student')

class high_schoolAdmin(admin.ModelAdmin) :
    link_display = ('student')

class gradeAdmin(admin.ModelAdmin) :
    link_display = ('student','Subject','grade')

admin.site.register(Teache_subject_Class,Teache_subject_ClassAdmin)
admin.site.register(primary_school,primary_schoolAdmin)
admin.site.register(high_school,high_schoolAdmin)
admin.site.register(gradesheet,gradeAdmin)

