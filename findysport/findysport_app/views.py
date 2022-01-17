from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from findysport_app.models import Usuario, Actividad, Local, Encargado, Apuntado, Grupo

class UsuarioListView(ListView):
    model = Usuario
class ActividadListView(ListView):
    model = Actividad
class LocalListView(ListView):
    model = Publisher