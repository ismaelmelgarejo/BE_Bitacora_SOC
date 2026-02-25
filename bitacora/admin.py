from django.contrib import admin
from . import models

# Ajusta los nombres según como inspectdb los haya creado
admin.site.register(models.Clientes)
admin.site.register(models.Proyectos)
admin.site.register(models.Tecnicos)
admin.site.register(models.Modalidades)
admin.site.register(models.Eventos)
admin.site.register(models.BitacoraSoc)

# Register your models here.
