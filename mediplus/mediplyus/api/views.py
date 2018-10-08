from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView
from mediplyus.models import Doctor
from .serializers import DoctorModelSerializer,DoctorModelCreateSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser


class DoctorListAPIView(ListAPIView):
    queryset=Doctor.objects.all()
    serializer_class=DoctorModelSerializer


class DoctorDetailAPIView(RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorModelSerializer


class DoctorUpdateAPIView(UpdateAPIView):
    queryset = Doctor.objects.all()
    permission_classes=[IsAdminUser]
    serializer_class = DoctorModelSerializer


class DoctorDeleteAPIView(DestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorModelSerializer
    permission_classes = [IsAdminUser]

class DoctorCreateAPIView(CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorModelCreateSerializer
    permission_classes = [IsAdminUser]