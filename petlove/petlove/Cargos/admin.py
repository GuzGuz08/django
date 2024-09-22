from django.contrib import admin
from .models import Cargos
# Register your models here.



class Cargosadmin(admin.ModelAdmin):
    list_display=('Codigo_Cargo_id', 'Descripcion')
    ordering=('Codigo_Cargo_id',)
    search_fields=('Codigo_Cargo_id', 'Descripcion')
    #list_editable=('Nombre','Precio','Descripcion')
    list_filter = ('Descripcion',)
    list_per_page = 5 #paginacion
    





admin.site.register(Cargos,Cargosadmin)


