from django.contrib import admin
from .models import Raza

# Register your models here.
class RazaAdmin(admin.ModelAdmin):

    list_display = ('desc_raza', 'estado')


admin.site.register(Raza, RazaAdmin) 
