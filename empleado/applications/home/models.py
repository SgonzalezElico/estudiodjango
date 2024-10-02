from django.db import models

# Create your models here.

#creamos la base de datos 
class Prueba(models.Model):
    #ponemos el titulo de la base de datos
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
