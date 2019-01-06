from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    is_doctor=models.BooleanField(default=False)
    is_ordinary=models.BooleanField(default=False)


class OrdinaryUser(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return "{name} {surname} ".format(name=self.first_name , surname=self.last_name)

