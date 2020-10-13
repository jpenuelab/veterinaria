from .models import TipoMascota
from .serializers import TipoSerializer
from rest_framework import viewsets

# Create your views here.

class TipoViewSet(viewsets.ModelViewSet):
    serializer_class = TipoSerializer
    queryset = TipoMascota.objects.all()

