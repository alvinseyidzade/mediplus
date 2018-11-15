from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
app_name='doctor'
urlpatterns = [
    url(r'^login/$', views.doctor_login_view, name="user_login"),
    url(r'^register/$', views.doctor_register_view, name="user_register"),
    url(r'^logout/$', views.doctor_log_out, name="logout"),
]
