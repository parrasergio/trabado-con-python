from django.db import models


class Familiar(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    fechaDeNacimiento = models.DateField()
    
class Madre(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    fechaDeNacimiento = models.DateField()
    
class Padre(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    fechaDeNacimiento = models.DateField()
    
class Hija(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    fechaDeNacimiento = models.DateField()