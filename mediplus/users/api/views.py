from rest_framework import generics

from users import models
from . import serializers

# class NormalUserListView(generics.ListCreateAPIView):
#     queryset = models.NormalUser.objects.all()
#     serializer_class = serializers.NormalUserSerializer
#
# class DoctorUserListView(generics.ListCreateAPIView):
#     queryset = models.DoctorUser.objects.all()
#     serializer_class = serializers.DoctorUserSerializer