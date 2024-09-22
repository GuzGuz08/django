from django.db import models

# Create your models here.

class Servicios(models.Model):
    Codigo_Servicio = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=150)
    Precio = models.DecimalField(max_digits = 20,decimal_places=2)
    Descripcion = models.CharField(max_length=150)
    