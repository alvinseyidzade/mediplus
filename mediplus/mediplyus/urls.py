from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import *
urlpatterns = [
    url(r'^list/$', list_view, name="list"),
    url(r'^(?P<slug>[\w-]+)/detail$', DocDetailview.as_view(), name='detail'),
]