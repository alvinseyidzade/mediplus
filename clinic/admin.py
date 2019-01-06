from django.contrib import admin
from .models import *

# Register your models here.
class AdminClinic(admin.ModelAdmin):
    display_list = ('name', 'doctor', 'slug')
admin.site.register(Clinic,AdminClinic)
