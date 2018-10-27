from django import forms
from .models import Post
from django.shortcuts import render
from django.urls import reverse
from .models import Comment
class FormPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'user',
            'title',
            'content',
            'image',
            'draft',
        ]
