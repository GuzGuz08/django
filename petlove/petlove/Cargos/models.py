from django.db import models

# Create your models here.


class Cargos(models.Model):
    Codigo_Cargo_id = models.IntegerField(primary_key=True)
    Descripcion = models.CharField(max_length=150)