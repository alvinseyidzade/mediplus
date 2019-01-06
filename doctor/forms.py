
from django import forms
from .models import Doctor
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

class DoctorForm(forms.ModelForm):
    password=forms.CharField(max_length=56)

    class Meta:
        model=User
        fields=('username', 'email', 'password', 'is_doctor')
class DoctorProfile(forms.ModelForm):
    age = forms.IntegerField()

    class Meta:
        model = Doctor
        fields = ('age', 'speciality', 'image','Stage','name','Level','clinic')






