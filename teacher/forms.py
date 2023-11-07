from django import forms
from tinymce.models import HTMLField
from django.contrib.auth.forms import UserCreationForm
from Main.models import *
from .models import *

class assignment_form(forms.ModelForm) :
    class Meta:
        model = Assignments
        fields = ('title','link_toupload')