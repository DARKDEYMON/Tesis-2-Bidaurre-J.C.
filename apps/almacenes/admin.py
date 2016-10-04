from django.contrib import admin
from apps.almacenes.models import *

# Register your models here.
admin.site.register(almacen)
admin.site.register(material)
admin.site.register(ingreso_material)
admin.site.register(herramientas)
admin.site.register(herramientasAlmacen)
admin.site.register(proveedor)

admin.site.register(insumos)
admin.site.register(insumosAlmacen)
admin.site.register(ingresoInsumos)
admin.site.register(salidaInsumos)