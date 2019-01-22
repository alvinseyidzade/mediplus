from rest_framework import generics

#from users import models
#from . import serializers

# class NormalUserListView(generics.ListCreateAPIView):
#     queryset = models.NormalUser.objects.all()
#     serializer_class = serializers.NormalUserSerializer
#
# class DoctorUserListView(generics.ListCreateAPIView):
#     queryset = models.DoctorUser.objects.all()
#     serializer_class = serializers.DoctorUserSerializer
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .serializers import ChangePasswordSerializer
from users.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView

class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = self.request.user
        return obj

    def update(self, request):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            if not self.object.check_password(serializer.data.get("old_password")):
                return HttpResponse({"old_password": ["Wrong password."]}, status= status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return HttpResponse("Success.", status=status.HTTP_200_OK)

        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)