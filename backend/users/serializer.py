from rest_framework import serializers
from . import services
from .models import User
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    role= serializers.CharField(read_only=True)
    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return services.UserDataClass(**data)