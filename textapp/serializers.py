from .models import *
from rest_framework import serializers


class TextInferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextInference
        fields = '__all__'
