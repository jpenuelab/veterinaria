from django.db import models
from raza.models import Raza
# Create your models here.

class Citas(models.Model):
    mascota = models.CharField(max_length=255)
    edad = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    amo = models.CharField(max_length=255)
    motivo = models.TextField(max_length=2000)
    estado = models.IntegerField()
    raza = models.ForeignKey(Raza, models.DO_NOTHING, db_column='raza')

    class Meta:
        db_table = 'citas'