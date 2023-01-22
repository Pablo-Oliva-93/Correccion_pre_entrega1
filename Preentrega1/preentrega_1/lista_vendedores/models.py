from django.db import models

# Create your models here.

class Vendedor (models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.FloatField()
    activo = models.BooleanField(default=True)