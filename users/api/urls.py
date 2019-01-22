from django.conf.urls import url
from .views import ChangePasswordView,ChangeUsernameView

urlpatterns = [
    url(r'^change/password/$', ChangePasswordView.as_view() , name="passupd"),
    url(r'^change/username/$', ChangeUsernameView.as_view() , name="passupd")
]