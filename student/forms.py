from django import forms
from tinymce.models import HTMLField
from django.contrib.auth.forms import UserCreationForm
from Main.models import *
from .models import *

class teacher_subject_form(forms.ModelForm):
    class Meta:
        model = Teache_subject_Class
        fields = ('teacher',)

class primary_form(forms.ModelForm):
    class Meta:
        model = primary_school
        fields = ('TELUGU','HINDI','ENGLISH','MATHS','SCIENCE')

class high_form(forms.ModelForm):
    class Meta:
        model = high_school
        fields = ('TELUGU','HINDI','ENGLISH','MATHS_A','MATHS_B','PHYSICS','CHEMISTRY','BIOLOGY')

class GradeUpdateForm(forms.ModelForm):
    class Meta:
        model = gradesheet
        fields = ['grade']  # Add the field(s) you want to update

