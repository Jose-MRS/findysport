from django.contrib import admin
from .models import Usuario, Actividad, Local, Encargado, Apuntado, Grupo

admin.site.register(Usuario)
admin.site.register(Actividad)
admin.site.register(Local)
admin.site.register(Encargado)
admin.site.register(Apuntado)
admin.site.register(Grupo)
# Register your models here.
