from rest_framework import serializers
from .models import CustomUser,Team,Challenge,Sports

class CustomUserSerializzers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'