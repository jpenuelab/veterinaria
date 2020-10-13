from django.contrib import admin
from .models import Citas

# Register your models here.
class CitasAdmin(admin.ModelAdmin):

    list_display = ('mascota', 'edad', 'amo')


admin.site.register(Citas, CitasAdmin) 
