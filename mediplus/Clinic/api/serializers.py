from rest_framework.serializers import ModelSerializer

from Clinic.models import Clinic

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
