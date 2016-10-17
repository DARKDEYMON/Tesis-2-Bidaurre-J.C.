from django.db import models

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from apps.almacenes.models import material, insumos, herramientas, maquinaria_equipo

from django.utils.translation import ugettext_lazy as _

# Create your models here.

class proyecto(models.Model):
	objeto_de_la_contratacion = models.CharField(
		max_length=100,
		blank=False, 
		null=False
	)
	modalidad_de_contratacion = models.CharField(
		max_length=100,
		blank=False,
		null=False
	)
	entidad_contratante = models.CharField(
		max_length=100,
		blank=False,
		null=False
	)
	ec_telefono = models.PositiveIntegerField(
		null=False, 
		blank=False, 
		validators=[
			RegexValidator(
				regex=r'^[0-9]{7,8}$', 
				message='El telefono tiene un maximo de 8 dijitos', 
				code='Numero Invalido'
			)
		]
	)
	ec_direccion = models.CharField(
		max_length=50,
		null=False,
		blank=False
	)
	ec_email = models.EmailField(
		null=False,
		blank=False
	)
	fecha_inicio = models.DateField(
		null=False,
		blank=False
	)
	plazo_previsto = models.DateField(
		null=False,
		blank=False
	)
	ubicacion_proyecto = models.CharField(
		max_length=2,
		null=False,
		blank=False,
		choices=(('PT','Potosi'),('LP','La Paz'),('CO','Cochabamba'),('CH','Chuquisaca'),('TA','Tarija'),('OR','Oruro'),('SC','Santa Cruz'),('BE','Beni'),('PA','Pando'))
	)
	presupuesto_final = models.FloatField(
		null=False,
		blank=False
	)
	def __str__(self):
		return (self.objeto_de_la_contratacion)

class item(models.Model):
	proyecto = models.ForeignKey(proyecto)
	descripcion = models.CharField(
		null=False,
		blank=False,
		max_length=120
	)
	fecha_inicio = models.DateField(
		null=False,
		blank=False
	)
	plazo_finalizacion = models.DateField(
		null=False,
		blank=False
	)
	unidad = models.CharField(
		max_length=3,
		null=False,
		blank=False,
		choices =(('Gbl','Gbl'),('m2','m2'),('m3','m3'))
	)
	cantidad = models.PositiveIntegerField(
		null=False,
		blank=False
	)
	def __str__(self):
		return (self.proyecto.objeto_de_la_contratacion+':'+self.descripcion)
	class Meta:
		#verbose_name = _('actividad')
		verbose_name_plural = _('items')
class peticion_materiales(models.Model):
	item = models.ForeignKey(item)
	material = models.ForeignKey(material)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False
	)
	precio_estimado_total = models.FloatField(
		blank=False,
		null=False
	)
	petion_de_planificacion = models.BooleanField(
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		blank=True,
		null=True
	)
	def __str__(self):
		return (self.material.decripcion)

class peticion_insumos(models.Model):
	item = models.ForeignKey(item)
	insumos = models.ForeignKey(insumos)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False
	)
	precio_estimado_total = models.FloatField(
		blank=False,
		null=False
	)
	petion_de_planificacion = models.BooleanField(
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		blank=True,
		null=True
	)
	def __str__(self):
		return (self.insumos.decripcion)

class peticion_Herramientas(models.Model):
	item = models.ForeignKey(item)
	herramientas = models.ForeignKey(herramientas)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False
	)
	petion_de_planificacion = models.BooleanField(
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		blank=True,
		null=True
	)
	def __str__(self):
		return (self.herramientas.decripcion)

class peticion_maquinaria_equipo(models.Model):
	item = models.ForeignKey(item)
	maquinaria_equipo = models.ForeignKey(maquinaria_equipo)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		blank=True,
		null=True
	)
	petion_de_planificacion = models.BooleanField(
		blank=False,
		null=False
	)
	def __str__(self):
		return (self.maquinaria_equipo.decripcion)
#externos
class requerimiento_personal(models.Model):
	item = models.ForeignKey(item)
	funcion = models.CharField(
		max_length=60,
		blank=False,
		null=False
	)
	cantidad = models.PositiveIntegerField(
		null=False,
		blank=False
	)
	precio_total = models.FloatField(
		null=False,
		blank=False
	)
	observaciones = models.TextField(
		blank=True,
		null=True
	)
	def __str__(self):
		return (self.funcion)

class requerimiento_maq_he(models.Model):
	item = models.ForeignKey(item)
	nombre_maq_he = models.CharField(
		max_length=60,
		blank=False,
		null=False
	)
	cantidad = models.PositiveIntegerField(
		null=False,
		blank=False
	)
	precio_total = models.FloatField(
		null=False,
		blank=False
	)
	observaciones = models.TextField(
		blank=True,
		null=True
	)
	def __str__(self):
		return (self.nombre_maq_he)

class materiales_locales(models.Model):
	item = models.ForeignKey(item)
	descripcion = models.CharField(
		max_length=60,
		blank=False,
		null=False
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False
	)
	precio_total = models.FloatField(
		blank=False,
		null=False,
	)
	def __str__(self):
		return (self.descripcion)
# reportes
class reportes_avance(models.Model):
	item = models.ForeignKey(item)
	date = models.DateField(
		blank=False,
		null=False,
		auto_now=True
	)
	alto = models.FloatField(
		null = False,
		blank = False,
		default = 0.0
	)
	largo = models.FloatField(
		null = False,
		blank = False,
		default = 0.0
	)
	ancho = models.FloatField(
		null = False,
		blank = False,
		default = 0.0
	)
	def __str__(self):
		return (self.item.descripcion)

def validate_file_extension(value):
	import os
	ext = os.path.splitext(value.name)[1]
	valid_extensions = ['.jpg','.png']
	if not ext in valid_extensions:
		raise ValidationError(u'Tipo de Archibo no Soportado!')
		
class reporte_fotografico(models.Model):
	reportes_avance = models.ForeignKey(reportes_avance)
	curriculum = models.FileField(
		upload_to='reporte_fotos/', 
		validators=[validate_file_extension],
		null=True,
		blank=True
	)