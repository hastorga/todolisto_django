from django.contrib import admin
from .models import Tarea, TipoTarea

# Register your models here.
#Esto carga los modelos al panel de administración de django
admin.site.register(Tarea)
admin.site.register(TipoTarea)

