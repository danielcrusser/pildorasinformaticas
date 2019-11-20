from django.db import models

class Persona(models.Model):

    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
  

