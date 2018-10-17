from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView
from mediplyus.models import Doctor,Clinic
from .serializers import DoctorModelSerializer,DoctorModelCreateSerializer,ClinicModelCreateSerializer,ClinicModelSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser


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





class ClinicListAPIView(ListAPIView):
    def get_queryset(self):
        queryset = Clinic.objects.all()
        location= self.request.query_params.get('location', None)
        name=self.request.query_params.get('name', None)


        if location is not None:
            queryset = queryset.filter(location=location)

        elif name is not None:
            queryset = queryset.filter(name=name)



        return queryset
    serializer_class=ClinicModelSerializer


class ClinicDetailAPIView(RetrieveAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicModelSerializer


class ClinicUpdateAPIView(UpdateAPIView):
    queryset = Clinic.objects.all()
    permission_classes=[IsAdminUser]
    serializer_class = ClinicModelSerializer


class ClinicDeleteAPIView(DestroyAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicModelSerializer
    permission_classes = [IsAdminUser]

class ClinicCreateAPIView(CreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicModelCreateSerializer
    permission_classes = [IsAdminUser]

