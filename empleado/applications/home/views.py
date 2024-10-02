from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.
#aca se hace la logica 

class IndexView(TemplateView):
    template_name = 'home/home.html'


class PruebaListView(ListView):
    #nombramos el archivo html en el que queremos que se plasme el resultado final
    template_name = 'home/lista.html'
    #que vamos a listar
    queryset = ['a','b','c']
    #ponemos el context para poder acceder a la variable
    context_object_name = "lista_prueba"