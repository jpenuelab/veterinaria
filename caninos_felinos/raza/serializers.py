from rest_framework import serializers
from .models import Raza


class RazaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Raza
        # fields = ['nombre_eps','estado']
        fields = ['id','desc_raza','estado','id_tipo']
