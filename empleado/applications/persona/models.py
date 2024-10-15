from django.db import models
#
from applications.departamento.models import Departamento

class Habilidades(models.Model):

    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'


    def __str__(self):
        return str(self.id) + '-' + self.habilidad


# Create your models here.
class Empleado(models.Model):
    """modelo para tabla empleado"""
    job_choices = (

        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO'),

    )
    #contador
    #administrador
    #economista
    #otro
    first_name = models.CharField("Nombre", max_length=50)
    last_name = models.CharField("Apellido", max_length=50)
    """atributos seleccionable"""
    job = models.CharField("Trabajo", max_length=1,choices=job_choices)
    #clave foranea
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado',blank=True,null=True)
    Habilidades = models.ManyToManyField(Habilidades)

    class Meta:

        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleado de la empresa'
        ordering = ['-first_name', 'departamento']
        unique_together = ('first_name','departamento')



    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
