from django.db import models

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from apps.almacenes.models import material, insumos

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
	plaso_previsto = models.DateField(
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
	plaso_finalisacion = models.DateField(
		null=False,
		blank=False
	)
	unidad = models.CharField(
		max_length=3,
		null=False,
		blank=False
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
	precio_estimado_total = models.PositiveIntegerField(
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
	precio_estimado_total = models.PositiveIntegerField(
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		blank=True,
		null=True
	)
	def __str__(self):
		return (self.insumos.decripcion)

class requerimientoPersonal(models.Model):
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
	precio_estimado_total = models.PositiveIntegerField(
		null=False,
		blank=False
	)
	observaciones = models.TextField(
		blank=True,
		null=True
	)
	def __str__(self):
		return (self.funcion)