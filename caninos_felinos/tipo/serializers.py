from rest_framework import serializers
from .models import TipoMascota


class TipoSerializer(serializers.ModelSerializer):
    razas = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = TipoMascota
        # fields = ['nombre_eps','estado']
        fields = ['id','desc_mascota','estado','razas']
