from django.db import models

# Create your models here.
#aca creamos la base de datos

class Departamento(models.Model):
    #en los parentesis pondemos el el nombre que queremos visualizar en django 
    name = models.CharField("Nombre", max_length=50)
    short_name = models.CharField("Nombre_corto", max_length=20, unique=True)
    #campo para saber si un departamento esta anulado
    anulate = models.BooleanField("Anulado",default=False)
    
    #añadimos decoradores
    class Meta:
        verbose_name = 'Mi Departameto'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name']
        unique_together = ('name','short_name')

    def __str__(self):
        return str(self.id) + "-" + self.name + "-" + self.short_name

