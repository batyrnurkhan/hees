from rest_framework import serializers
from .models import Materials
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

class MaterialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Materials
        fields = "__all__"
        #("title", "content", "category")
        
