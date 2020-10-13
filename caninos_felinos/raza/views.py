from .models import Raza
from .serializers import RazaSerializer
from rest_framework import viewsets
# Create your views here.

class RazaViewSet(viewsets.ModelViewSet):
    serializer_class = RazaSerializer
    queryset = Raza.objects.all()
