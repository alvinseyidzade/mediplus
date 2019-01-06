from django.contrib import admin

from django.conf.urls import url, include
from .views import ClinicCreateAPIView,ClinicDeleteAPIView,ClinicDetailAPIView,ClinicListAPIView,ClinicUpdateAPIView
urlpatterns = [

    url(r'^list/$', ClinicListAPIView.as_view(), name="cliniclist"),
    url(r'^(?P<pk>\d+)/detail/$', ClinicDetailAPIView.as_view() , name="clinicdetail"),
    url(r'^(?P<pk>\d+)/update/$', ClinicUpdateAPIView.as_view() , name="clinicupdate"),
    url(r'^(?P<pk>\d+)/delete/$', ClinicDeleteAPIView.as_view() , name="clinicdelete"),
    url(r'^create/$', ClinicCreateAPIView.as_view() , name="cliniccreate"),
]