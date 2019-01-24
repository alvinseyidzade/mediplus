from django.contrib import admin

from django.conf.urls import url, include
from .views import DoctorDetailAPIView,DoctorListAPIView,DoctorDeleteAPIView,DoctorUpdateAPIView,DoctorCreateAPIView,DoctorProfileChangeAPIView

urlpatterns = [
    url(r'^list/$', DoctorListAPIView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/detail/$', DoctorDetailAPIView.as_view() , name="docdetail"),
    url(r'^(?P<pk>\d+)/update/$', DoctorUpdateAPIView.as_view() , name="docupdate"),
    url(r'^(?P<pk>\d+)/delete/$', DoctorDeleteAPIView.as_view() , name="docdel"),
    url(r'^create/$', DoctorCreateAPIView.as_view() , name="doccre"),
    url(r'^change/profile-info/$', DoctorProfileChangeAPIView.as_view() , name="docproup" )

]