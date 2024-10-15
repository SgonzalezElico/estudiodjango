from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (

        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',

    )

    """
    Funcion extra de decoradores de django para agregar datos extra que no estan en el modelo en este caso se hizo un funcion para retornar el nombre completo

    def full_name(self,obj):
        return  obj.first_name + '-' + obj.last_name
    """
    def full_name(self,obj):

        print(obj.first_name)
        return  obj.first_name + '-' + obj.last_name
    """
        los filtros en el admin se ponen con  search_fields = ('nombre de un parametro del list display',)
    """
    search_fields = ('first_name',)

    """
        para poner un filtrador list_filter = ('parametro que se quiere buscar')
    """
    list_filter = ('job','Habilidades',)
    """
    Filtro horizontal, este campo solo sirve para relacion de muchos a muchos
    """
    filter_horizontal = ('Habilidades',)

admin.site.register(Empleado, EmpleadoAdmin) 