from django import forms
from tinymce.models import HTMLField
from django.contrib.auth.forms import UserCreationForm
from Main.models import *


class login(forms.Form) :     # forms.Form(for Creating a new form )  simillar to  models.Model(for Creating Sql Auery)
    username = forms.CharField(label = "userName",required = True , max_length=15,widget = forms.TextInput(attrs={'class' : "form-control",'style':'max-width: 12em'}) )
    password = forms.CharField(
        label="Password",
        required=True,
        max_length=20,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'max-width: 12em',
            'pattern': '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$',
            'title': 'Password must contain at least one lowercase letter, one capital letter, and one number.',
        })
    )
    # role = forms.ChoiceField(
    #     label='Role',
    #     choices=[('none', 'Select Type'), ('teacher', 'Teacher'), ('student', 'Student')],
    #     widget=forms.Select
    #     (attrs={
    #         'id': 'user-type','class': 'form-control',
    #         'style': 'max-width: 12em',})
    # )

class user(UserCreationForm):
    class Meta :
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'country_code', 'phone_number', 'father_name', 'mother_name', 'Permanent_address']
























































 # COUNTRY_CODE_CHOICES = [
    #     ('+91', 'India (+91)'),
    #     ('+1', 'United States (+1)'),
    #     # Add more country code choices as needed
    # ]
    # photo = forms.FileField(label = "Profile Photo" )
    # class Meta:
    #     model = Profile
    #     fields = ['photo']
    # first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # surname = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    # age = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # gender = forms.ChoiceField(
    #     choices=[('none', 'Select Gender'), ('male', 'Male'), ('female', 'Female'), ('trans', 'Other')],
    #     widget=forms.Select(attrs={'class': 'form-control'}),
    #     required=True
    # )
    # country_code = forms.ChoiceField(choices=COUNTRY_CODE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    # phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # father_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # mother_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # # Define your password and confirm_password fields here
    # password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
    #         'class': 'form-control',
    #         'style': 'max-width: 12em',
    #         'pattern': '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$',
    #         'title': 'Password must contain at least one lowercase letter, one capital letter, and one number.',
    #     }), required=True)
    # confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
    #         'class': 'form-control',
    #         'style': 'max-width: 12em',
    #         'pattern': '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$',
    #         'title': 'Password must contain at least one lowercase letter, one capital letter, and one number.',
    #     }), required=True)
    # Permanent_address = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # class Meta:
    #     model = Profile
    #     fields = ['date_of_birth','photo']
    # for password conformatio