from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
app_name='users'
urlpatterns = [
    url(r'^login/$', views.user_login_view, name="ordinaryuser_login"),
    url(r'^register/$', views.user_register_view, name="ordinary_register"),
    url(r'^logout/$', views.ordinary_log_out, name="ordinary_logout"),
]
