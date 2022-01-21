"""findysport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from findysport_app.views import ActividadCreateView, ActividadDeleteView, ActividadUpdateView
from findysport_app.views import ApuntadoCreateView, ApuntadoDeleteView, ApuntadoUpdateView
from findysport_app.views import EncargadoCreateView, EncargadoDeleteView, EncargadoUpdateView
from findysport_app.views import GrupoCreateView, GrupoDeleteView, GrupoUpdateView
from findysport_app.views import LocalCreateView, LocalDeleteView, LocalUpdateView

from findysport_app.views import UsuarioListView, ActividadListView, LocalListView, EncargadoListView, ApuntadoListView, GrupoListView
from findysport_app.views import UsuarioDetailView, ActividadDetailView, LocalDetailView, EncargadoDetailView, ApuntadoDetailView, GrupoDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', UsuarioListView.as_view(), name = "usuario-list"),
    path('actividad/', ActividadListView.as_view(), name = "actividad-list"),
    path('local/', LocalListView.as_view(), name = "local-list"),
    path('encargado/', EncargadoListView.as_view(), name = "encargado-list"),
    path('apuntado/', ApuntadoListView.as_view(), name = "apuntado-list"),
    path('grupo/', GrupoListView.as_view(), name = "grupo-list"),
    
    path('usuario/<int:pk>/', UsuarioDetailView.as_view(), name = "usuario-detail"),
    path('actividad/<int:pk>/', ActividadDetailView.as_view(), name = "actividad-detail"), 
    path('local/<int:pk>/', LocalDetailView.as_view(), name = "local-detail"),
    path('encargado/<int:pk>/', EncargadoDetailView.as_view(), name = "encargado-detail"),
    path('apuntado/<int:pk>/', ApuntadoDetailView.as_view(), name = "apuntado-detail"),
    path('grupo/<int:pk>/', GrupoDetailView.as_view(), name = "grupo-detail"),

    path('actividad/add/', ActividadCreateView.as_view(), name='actividad-add'),
    path('actividad/<int:pk>/', ActividadUpdateView.as_view(), name='actividad-update'),
    path('actividad/<int:pk>/delete/', ActividadDeleteView.as_view(), name='actividad-delete'),
    
    path('apuntado/add/', ApuntadoCreateView.as_view(), name='apuntado-add'),
    path('apuntado/<int:pk>/', ApuntadoUpdateView.as_view(), name='apuntado-update'),
    path('apuntado/<int:pk>/delete/', ApuntadoDeleteView.as_view(), name='apuntado-delete'),

    path('encargado/add/', EncargadoCreateView.as_view(), name='encargado-add'),
    path('encargado/<int:pk>/', EncargadoUpdateView.as_view(), name='encargado-update'),
    path('encargado/<int:pk>/delete/', EncargadoDeleteView.as_view(), name='encargado-delete'),

    path('grupo/add/', GrupoCreateView.as_view(), name='grupo-add'),
    path('grupo/<int:pk>/', GrupoUpdateView.as_view(), name='grupo-update'),
    path('grupo/<int:pk>/delete/', GrupoDeleteView.as_view(), name='grupo-delete'), 
    
    path('local/add/', LocalCreateView.as_view(), name='local-add'),
    path('local/<int:pk>/', LocalUpdateView.as_view(), name='local-update'),
    path('local/<int:pk>/delete/', LocalDeleteView.as_view(), name='local-delete'),
]
