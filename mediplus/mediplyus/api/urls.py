from django.contrib import admin

from django.conf.urls import url, include
from .views import DoctorDetailAPIView,DoctorListAPIView,DoctorDeleteAPIView,DoctorUpdateAPIView,DoctorCreateAPIView
urlpatterns = [
    url(r'^list/$', DoctorListAPIView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/detail/$', DoctorDetailAPIView.as_view() , name="detail"),
    url(r'^(?P<pk>\d+)/update/$', DoctorUpdateAPIView.as_view() , name="detail"),
    url(r'^(?P<pk>\d+)/delete/$', DoctorDeleteAPIView.as_view() , name="detail"),
    url(r'^create/$', DoctorCreateAPIView.as_view() , name="detail"),
]