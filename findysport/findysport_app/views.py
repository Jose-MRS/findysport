#Create your views here.

from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.views.generic import ListView, DetailView
from findysport_app.models import Usuario, Actividad, Local, Encargado, Apuntado, Grupo

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

def index(request):
    return render(request, 'index.html')

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

#-----------VISTAS CREATE UPDATE DELETE-----------------
class ActividadCreateView(CreateView):
    model = Actividad
    fields = ['nombre', 'local', 'tipo', 'descripcion', 'creador']
    success_url = reverse_lazy('actividad-list')

class ActividadUpdateView(UpdateView):
    model = Actividad
    fields = ['nombre', 'local', 'tipo', 'descripcion', 'creador']
    success_url = reverse_lazy('actividad-list')

class ActividadDeleteView(DeleteView):
    model = Actividad
    success_url = reverse_lazy('actividad-list')
#---------------------------------------------------------------------------------
class ApuntadoCreateView(CreateView):
    model = Apuntado
    fields = ['actividad', 'grupo']
    success_url = reverse_lazy('apuntado-list')

class ApuntadoUpdateView(UpdateView):
    model = Apuntado
    fields = ['actividad', 'grupo']
    success_url = reverse_lazy('apuntado-list')

class ApuntadoDeleteView(DeleteView):
    model = Apuntado
    success_url = reverse_lazy('apuntado-list')
#----------------------------------------------------------------------------------
class EncargadoCreateView(CreateView):
    model = Encargado
    fields = ['nombre_en', 'actividad']
    success_url = reverse_lazy('encargado-list')

class EncargadoUpdateView(UpdateView):
    model = Encargado
    fields = ['nombre_en', 'actividad']
    success_url = reverse_lazy('encargado-list')

class EncargadoDeleteView(DeleteView):
    model = Encargado
    success_url = reverse_lazy('encargado-list')
#--------------------------------------------------------------------------------------
class GrupoCreateView(CreateView):
    model = Grupo
    fields = ['nombre', 'actividad', 'horas', 'encargado', 'espacio_max']
    success_url = reverse_lazy('grupo-list')

class GrupoUpdateView(UpdateView):
    model = Grupo
    fields = ['nombre', 'actividad', 'horas', 'encargado', 'espacio_max']
    success_url = reverse_lazy('grupo-list')

class GrupoDeleteView(DeleteView):
    model = Grupo
    success_url = reverse_lazy('grupo-list')
#--------------------------------------------------------------------------------------
class LocalCreateView(CreateView):
    model = Local
    fields = ['nombre_local', 'direccion_local', 'ciudad']
    success_url = reverse_lazy('local-list')

class LocalUpdateView(UpdateView):
    model = Local
    fields = ['nombre_local', 'direccion_local', 'ciudad']
    success_url = reverse_lazy('local-list')

class LocalDeleteView(DeleteView):
    model = Local
    success_url = reverse_lazy('local-list')
#--------------------------------------------------------------------------------------
'''class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)'''