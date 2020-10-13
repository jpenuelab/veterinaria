from django.contrib import admin
from .models import TipoMascota

# Register your models here.
class TipoMascotaAdmin(admin.ModelAdmin):

    list_display = ('desc_mascota', 'estado')


admin.site.register(TipoMascota, TipoMascotaAdmin) 
