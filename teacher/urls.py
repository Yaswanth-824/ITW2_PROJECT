from django.urls import path,include

from . import views
# from . import forms
# from . import models

urlpatterns = [
    path('',views.home,name = 'home'),
    path('Attendence/',views.Attendence,name = 'Attendence'),
    path('update/',views.update,name= 'update'),
    path('updateprofile/',views.updateprofile,name = 'updateprofile'),
    path('updateduedate/',views.updateduedate,name = 'updateduedate'),
    path('gradeupdate/',views.gradeupdate,name = 'gradeupdate'),
    path('assignment/',views.assignment,name = 'assignment'),
    path('delete/',views.deleteAssignment,name = 'delete' ),
    path('StudentsDetails/',views.StudentsDetails,name = 'StudentsDetails'),
    path('profile/',views.profile,name = 'profile'),
    path('gallery/',views.gallery,name = 'gallery'),  #for Gallery
    path('contact/',views.contact,name = 'contact'),    # for Contact
    path('about-us/',views.about_us,name = 'about-us'),
]