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
from findysport_app.views import UsuarioListView, ActividadListView, LocalListView, EncargadoListView, ApuntadoListView, GrupoListView
from findysport_app.views import UsuarioDetailView, ActividadDetailView, LocalDetailView, EncargadoDetailView, ApuntadoDetailView, GrupoDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', UsuarioListView.as_view(), name = "Usuario-list"),
    path('actividades/', ActividadListView.as_view()),
    path('locales/', LocalListView.as_view()),
    path('encargados/', EncargadoListView.as_view()),
    path('apuntados/', ApuntadoListView.as_view()),
    path('grupos/', GrupoListView.as_view()),
    path('usuario/<int:pk>/', UsuarioDetailView.as_view()),
    path('actividad/<int:pk>/', ActividadDetailView.as_view()),
    path('local/<int:pk>/', LocalDetailView.as_view()),
    path('encargado/<int:pk>/', EncargadoDetailView.as_view()),
    path('apuntado/<int:pk>/', ApuntadoDetailView.as_view()),
    path('grupo/<int:pk>/', GrupoDetailView.as_view()),
]
