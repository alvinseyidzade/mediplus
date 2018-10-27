from rest_framework.serializers import ModelSerializer

from Doctor.models import Doctor

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
