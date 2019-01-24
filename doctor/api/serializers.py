from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from doctor.models import Doctor

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
class DoctorChangeProfileSerializer(serializers.ModelSerializer):
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
