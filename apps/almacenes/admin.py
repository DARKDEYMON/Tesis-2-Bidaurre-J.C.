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