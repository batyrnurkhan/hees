from rest_framework import serializers
from users import serializer as user_serializer
from . import services

class ResumeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField()
    date_published = serializers.DateTimeField(read_only=True)
    user = user_serializer.UserSerializer(read_only=True)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.ResumeDataClass(**data)