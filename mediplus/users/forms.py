from django import forms
from .models import OrdinaryUser

from django.contrib.auth import get_user_model
User = get_user_model()
class OrdinaryUserForm(forms.ModelForm):

    class Meta:
        model=User
        fields=('username', 'email', 'password', 'is_ordinary')

class OrdinaryUserProfile(forms.ModelForm):
    class Meta:
        model=OrdinaryUser
        fields=("first_name","last_name")



