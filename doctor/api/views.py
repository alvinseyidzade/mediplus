from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView
from doctor.models import Doctor
from clinic.models import Clinic
from .serializers import DoctorModelSerializer,DoctorModelCreateSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .permissions import IsOwnerOrReadOnly

class DoctorListAPIView(ListAPIView):
    def get_queryset(self):
        queryset = Doctor.objects.all()
        clinic= self.request.query_params.get('clinic', None)
        name=self.request.query_params.get('name', None)
        speciality = self.request.query_params.get('speciality', None)

        if clinic is not None:
            queryset = queryset.filter(clinic=clinic)

        elif name is not None:
            queryset = queryset.filter(name=name)
        elif speciality is not None:
            queryset = queryset.filter(speciality=speciality)


        return queryset

    serializer_class=DoctorModelSerializer


class DoctorDetailAPIView(RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorModelSerializer


class DoctorUpdateAPIView(UpdateAPIView):


    queryset = Doctor.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DoctorModelSerializer


class DoctorDeleteAPIView(DestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorModelSerializer
    permission_classes = [IsAdminUser]

class DoctorCreateAPIView(CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorModelCreateSerializer
    permission_classes = [IsAdminUser]




