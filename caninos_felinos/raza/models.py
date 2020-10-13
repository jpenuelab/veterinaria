from django.db import models
from tipo.models import TipoMascota 

# Create your models here.


class Raza(models.Model):
    id = models.IntegerField(primary_key=True)
    desc_raza = models.CharField(max_length=255)
    estado = models.IntegerField()
    id_tipo = models.ForeignKey(TipoMascota, models.DO_NOTHING, db_column='id_tipo',related_name='razas')

    class Meta:
        db_table = 'raza'

    def __str__(self):
        return str(self.id)+"|"+self.desc_raza+"|"+str(self.estado)+"|"+str(self.id_tipo)