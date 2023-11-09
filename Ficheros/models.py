from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=128)
    año = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    
class Moto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=128)
    año = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()