from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name = 'home'),
    path('profile/',views.profile,name = 'profile'),
    path('Courses_Info/',views.course_info,name = 'course_info'),
    path('Viewassignment/',views.assignmentview,name = 'assignmentview'),
    path('updateprofile/',views.updateprofile,name = 'updateprofile'),
    path('register_course/',views.register_course,name = 'register_course'),
    path('GradeSheet/',views.Gradesheet,name = 'gradesheet'),
    path('gallery/',views.gallery,name = 'gallery'),  #for Gallery
    path('contact/',views.contact,name = 'contact'),    # for Contact
]