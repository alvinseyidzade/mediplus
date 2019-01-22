from django.conf.urls import url
from .views import ChangePasswordView

urlpatterns = [
    url(r'^change/password/$', ChangePasswordView.as_view() , name="passupd")
]