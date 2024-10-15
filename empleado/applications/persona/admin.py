from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.
from .models import Empleado
admin.site.register(Empleado)

admin.site.register(Habilidades) 