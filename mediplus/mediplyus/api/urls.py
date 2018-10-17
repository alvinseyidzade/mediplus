from django.contrib import admin

from django.conf.urls import url, include
from .views import DoctorDetailAPIView,DoctorListAPIView,DoctorDeleteAPIView,DoctorUpdateAPIView,DoctorCreateAPIView,ClinicCreateAPIView,ClinicDeleteAPIView,ClinicDetailAPIView,ClinicListAPIView,ClinicUpdateAPIView
urlpatterns = [
    url(r'^doctorlist/$', DoctorListAPIView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/doctordetail/$', DoctorDetailAPIView.as_view() , name="docdetail"),
    url(r'^(?P<pk>\d+)/doctorupdate/$', DoctorUpdateAPIView.as_view() , name="docupdate"),
    url(r'^(?P<pk>\d+)/doctordelete/$', DoctorDeleteAPIView.as_view() , name="docdel"),
    url(r'^doctorcreate/$', DoctorCreateAPIView.as_view() , name="doccre"),
    url(r'^cliniclist/$', ClinicListAPIView.as_view(), name="cliniclist"),
    url(r'^(?P<pk>\d+)/clinicdetail/$', ClinicDetailAPIView.as_view() , name="clinicdetail"),
    url(r'^(?P<pk>\d+)/clinicupdate/$', ClinicUpdateAPIView.as_view() , name="clinicupdate"),
    url(r'^(?P<pk>\d+)/clinicdelete/$', ClinicDeleteAPIView.as_view() , name="clinicdelete"),
    url(r'^cliniccreate/$', ClinicCreateAPIView.as_view() , name="cliniccreate"),
]