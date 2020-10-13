from django.db import models

# Create your models here.

class TipoMascota(models.Model):
    desc_mascota = models.CharField(max_length=255)
    estado = models.IntegerField()

    class Meta:
        db_table = 'tipo_mascota'

    def __str__(self):
        return self.desc_mascota