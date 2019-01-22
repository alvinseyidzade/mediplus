from rest_framework import serializers
# from users.models import NormalUser,DoctorUser
#
# class NormalUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NormalUser
#         fields = ('email', 'username', 'password' )
#
#
# class DoctorUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DoctorUser
#         fields = ('email', 'username', 'password')


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
class ChangeUsernameSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    new_username = serializers.CharField(required=True)

