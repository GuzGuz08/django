from django.contrib import admin
from .models import Empleados
# Register your models here.



class Empleadosadmin(admin.ModelAdmin):
    list_display=('Codigo_Empleado','Nombre','Apellido','Telefono','Email', 'Codigo_Cargo_id')
    ordering=('-Nombre',)
    search_fields=('Codigo_Empleado','Nombre','Apellido','Telefono','Email', 'Codigo_Cargo_id')
    #list_editable=('Nombre','Precio','Descripcion')
    list_filter = ('Nombre',)
    list_per_page = 5 #paginacion





admin.site.register(Empleados,Empleadosadmin)

