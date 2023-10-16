from rest_framework import serializers
from .models import *

class carSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields="__all__"