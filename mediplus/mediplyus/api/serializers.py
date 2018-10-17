from rest_framework.serializers import ModelSerializer

from mediplyus.models import Doctor,Clinic

class DoctorModelSerializer(ModelSerializer):
    class Meta:
        model=Doctor
        fields=[
            'name',
            'speciality',
            'Stage',
            'clinic',
            'Level',
            'image',
            'id',
        ]
class DoctorModelCreateSerializer(ModelSerializer):
    class Meta:
        model=Doctor
        fields=[
            'name',
            'speciality',
            'Stage',
            'clinic',
            'Level',
            'image',

        ]
class ClinicModelSerializer(ModelSerializer):
    class Meta:
        model=Clinic
        fields=[
            'name',
            'number',
            'location',
            'image',

        ]

class ClinicModelCreateSerializer(ModelSerializer):
    class Meta:
        model=Clinic
        fields=[
            'number',
            'name',
            'location',
            'image',
        ]
