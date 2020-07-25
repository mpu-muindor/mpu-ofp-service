from rest_framework import serializers
from .models import *

class GymmnasiumListSerializer(serializers.ModelSerializer):
    # Список физкультурных залов
    class Meta:
        model = Gymnasium
        fields = ("name", "address")

class GymnasiumDetailSerializer(serializers.ModelSerializer):
    # Детальное описание зала
    class Meta:
        model = Gymnasium
        fields = ("name", "address", "description")