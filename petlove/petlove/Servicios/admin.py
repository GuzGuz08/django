from django.contrib import admin
from .models import Servicios


# Register your models here.

class Serviciosadmin(admin.ModelAdmin):
    list_display=('Codigo_Servicio','Nombre','Precio','Descripcion')
    ordering=('-Nombre',)
    search_fields=('Codigo_Servicio','Nombre','Precio','Descripcion')
    #list_editable=('Nombre','Precio','Descripcion')
    list_filter = ('Precio',)
    list_per_page = 5 #paginacion





admin.site.register(Servicios,Serviciosadmin)

