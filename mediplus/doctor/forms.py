
from django import forms
from .models import Doctor
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User

class DoctorForm(forms.ModelForm):
    password=forms.CharField(max_length=56)

    class Meta:
        model=User
        fields=('username', 'email', 'password', )
class DoctorProfile(forms.ModelForm):
    age = forms.IntegerField()

    class Meta:
        model = Doctor
        fields = ('age', 'speciality', 'image','Stage')






