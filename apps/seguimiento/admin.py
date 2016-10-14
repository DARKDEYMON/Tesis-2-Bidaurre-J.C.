from django.contrib import admin
from apps.seguimiento.models import *

# Register your models here.
admin.site.register(proyecto)
admin.site.register(item)

admin.site.register(peticion_materiales)
admin.site.register(peticion_insumos)
admin.site.register(peticion_Herramientas)

admin.site.register(requerimiento_personal)
admin.site.register(requerimiento_maq_he)
admin.site.register(materiales_locales)