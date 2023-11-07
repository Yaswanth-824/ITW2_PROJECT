from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('gallery/',views.gallery,name = 'gallery'),  #for Gallery
    path('contact/',views.contact,name = 'contact'),    # for Contact
    path('about-us/',views.about_us,name = 'about-us'),
    path('forgot-password/',views.forgot_password,name ='forgot_password'),
    path("about_founder/",views.founder ,name = 'founder'),
    path('new-user/',views.new_user,name ='new_user'),
    path('register_user/',views.register_user,name ='register_user'),
    path('login/',views.sign_in,name = 'login'),
    path('logout/',views.sign_out,name = 'logout'),

    # path('logout/',auth_views.LogoutView.as_view(template_name='home/school_website.html'),name = 'logout'),
    # link after login
]