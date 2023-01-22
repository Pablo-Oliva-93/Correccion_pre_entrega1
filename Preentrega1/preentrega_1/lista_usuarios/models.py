from django.db import models

# Create your models here.

class Usuario (models.Model):
    usuario = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    edad = models.FloatField()
