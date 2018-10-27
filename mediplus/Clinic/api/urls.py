from django.contrib import admin

from django.conf.urls import url, include
from .views import ClinicCreateAPIView,ClinicDeleteAPIView,ClinicDetailAPIView,ClinicListAPIView,ClinicUpdateAPIView
urlpatterns = [

    url(r'^cliniclist/$', ClinicListAPIView.as_view(), name="cliniclist"),
    url(r'^(?P<pk>\d+)/clinicdetail/$', ClinicDetailAPIView.as_view() , name="clinicdetail"),
    url(r'^(?P<pk>\d+)/clinicupdate/$', ClinicUpdateAPIView.as_view() , name="clinicupdate"),
    url(r'^(?P<pk>\d+)/clinicdelete/$', ClinicDeleteAPIView.as_view() , name="clinicdelete"),
    url(r'^cliniccreate/$', ClinicCreateAPIView.as_view() , name="cliniccreate"),
]