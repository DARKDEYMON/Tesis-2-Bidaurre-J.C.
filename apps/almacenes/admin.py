from django.contrib import admin
from apps.almacenes.models import *

# Register your models here.
admin.site.register(almacen)
admin.site.register(proveedor)

admin.site.register(material)
admin.site.register(materialAlmacen)
admin.site.register(ingresoMaterial)
admin.site.register(salidaMaterial)

admin.site.register(insumos)
admin.site.register(insumosAlmacen)
admin.site.register(ingresoInsumos)
admin.site.register(salidaInsumos)

admin.site.register(herramientas)
admin.site.register(herramientasAlmacen)
admin.site.register(ingresoHerramientas)
admin.site.register(salidaHerramientas)

admin.site.register(maquinaria_equipo)
admin.site.register(maquinaria_equipoAlmacen)
admin.site.register(ingresoMaquinaria_equipo)
admin.site.register(salidaMaquinaria_equipo)

admin.site.register(tipoActivo)
admin.site.register(activo)