from django.db import models

# Create your models here.

class Empleados(models.Model):
    Codigo_Empleado = models.AutoField(primary_key=True)  # Cambia a AutoField
    Nombre = models.CharField(max_length=150)
    Apellido = models.CharField(max_length=150)
    Telefono = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    Codigo_Cargo = models.ForeignKey('Cargos.Cargos', on_delete=models.CASCADE)