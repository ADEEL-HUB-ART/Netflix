from .models import *
from rest_framework import serializers

class OtpSerializer(serializers.ModelSerializer):

    class Meta:
        models = OTP
        fields = ['otp_code']

    def create(self, validated_data):
        user = User.objects.create(otp_code = validated_data['otp_code'])
        user.save()
        return user