from rest_framework import serializers
from .models import Citas


class CitasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Citas
        # fields = ['nombre_eps','estado']
        fields = '__all__'
