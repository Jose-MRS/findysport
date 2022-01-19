#Create your views here.

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from findysport_app.models import Usuario, Actividad, Local, Encargado, Apuntado, Grupo

class UsuarioListView(ListView):
    model = Usuario   
class ActividadListView(ListView):
    model = Actividad
class LocalListView(ListView):
    model = Local
class EncargadoListView(ListView):
    model = Encargado
class ApuntadoListView(ListView):
    model = Apuntado
class GrupoListView(ListView):
    model = Grupo


class UsuarioDetailView(DetailView):
    context_object_name = 'usuario'
    queryset = Usuario.objects.all()

class ActividadDetailView(DetailView):
    context_object_name = 'actividad'
    queryset = Actividad.objects.all()

class LocalDetailView(DetailView):
    context_object_name = 'local'
    queryset = Local.objects.all()

class EncargadoDetailView(DetailView):
    context_object_name = 'encargado'
    queryset = Encargado.objects.all()

class ApuntadoDetailView(DetailView):
    context_object_name = 'apuntado'
    queryset = Apuntado.objects.all()

class GrupoDetailView(DetailView):
    context_object_name = 'grupo'
    queryset = Grupo.objects.all()