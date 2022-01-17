from django.db import models
from django.db.models import manager
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import OneToOneField

# Create your models here.
class Usuario(models.Model):
    edad = models.IntegerField()
    direccion = models.CharField(max_length=100)
    cod_postal = models.IntegerField()
    ciudad = models.CharField(max_length=20)
    dni = models.CharField(max_length=15)
    telefono = models.CharField(max_length=13)
    

class Local(models.Model):
    nombre_local = models.CharField(max_length=30)
    direccion_local = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre_local
    
class Actividad(models.Model):
    local = models.ForeignKey(Local, on_delete=CASCADE)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=16)
    descripcion = models.CharField(max_length=200)
    creador = models.CharField(max_length=20)
   
class Encargado(models.Model):
    nombre_en = models.CharField(max_length=30)
    actividad = models.ManyToManyField(Actividad)
class Grupo(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=CASCADE)
    nombre = models.CharField(max_length=30)
    horas = models.CharField(max_length=30)
    encargado = models.ForeignKey(Encargado, on_delete=CASCADE)
    espacio = models.IntegerField(default=0)
    espacio_max = models.IntegerField(default=15)

class Apuntado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=CASCADE)
    actividad = models.ManyToManyField(Actividad)
    grupo = models.ForeignKey(Grupo, on_delete=CASCADE)

   

