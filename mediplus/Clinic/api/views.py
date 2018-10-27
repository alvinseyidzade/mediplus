from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView
from Clinic.models import Clinic
from Doctor.models import Doctor
from .serializers import ClinicModelCreateSerializer,ClinicModelSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser






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

