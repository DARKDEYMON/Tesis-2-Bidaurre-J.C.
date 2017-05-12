from django.db import models
from django.apps import apps
from django.utils.translation import ugettext_lazy as _
#from apps.seguimiento.models import item

from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db.models import F
from django.db.models import Sum
from django.db.models import Avg

import re

# Create your models here.
class almacen(models.Model):
	ciudad = models.CharField(
		max_length=100,
		blank=False,
		null=False,
		unique=True,
		choices=(('PT','Potosi'),('LP','La Paz'),('CO','Cochabamba'),('CH','Chuquisaca'),('TA','Tarija'),('OR','Oruro'),('SC','Santa Cruz'),('BE','Beni'),('PA','Pando'))
	)
	direccion = models.CharField(
		max_length=100,
		blank=False,
		null=False
	)
	telefono = models.PositiveIntegerField(
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
	observaciones = models.TextField(
		null=True,
		blank=True,
	)
	def items(self):
		item = apps.get_model('seguimiento', 'item')
		return item.objects.filter(proyecto__ubicacion_proyecto=str(self.ciudad))
	def __str__(self):
		return self.ciudad

class proveedor(models.Model):
	rason_social = models.CharField(
		max_length=100,
		blank=False,
		null=False,
		unique=True
	)
	telefono = models.PositiveIntegerField(
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
	email = models.EmailField(
		null=False,
		blank=False
	)
	direccion = models.CharField(
		max_length=50,
		null=False,
		blank=False
	)
	observaciones = models.TextField(
		null=True,
		blank=True,
	)
	def __str__(self):
		return self.rason_social
	class Meta:
		verbose_name_plural = _('proveedores')
		
class material(models.Model):
	decripcion = models.CharField(
		max_length=100,
		blank=False,
		null=False,
		unique=True
	)
	unidad = models.CharField(
		max_length=10,
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		null=True,
		blank=True,
	)
	def clean(self):
		aux = re.sub(' +',' ',self.decripcion)
		self.decripcion = aux.capitalize()
	def __str__(self):
		return self.decripcion

class materialAlmacen(models.Model):
	almacen = models.ForeignKey(almacen)
	material = models.ForeignKey(material)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)
	def __str__(self):
		return self.material.decripcion
	class Meta:
		unique_together = (('almacen', 'material'),)

class ingresoMaterial(models.Model):
	almacen = models.ForeignKey(almacen)
	material = models.ForeignKey(material)
	proveedor = models.ForeignKey(proveedor)
	item = models.ForeignKey('seguimiento.item')
	no_factura = models.PositiveIntegerField(
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[0-9]{5,20}$', 
				message='El numero de factura tiene de 5 a 20 cifras', 
				code='Numero Invalido'
			)
		]
	)
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	costo_total = models.PositiveIntegerField(
		null=False,
		blank=False,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)
	def totalItem(self):
		res = ingresoMaterial.objects.filter(item=self.item).aggregate(total=Sum('costo_total'))
		return res['total']
	def total(self):
		item = apps.get_model('seguimiento', 'item')
		res = ingresoMaterial.objects.filter(item__in=item.objects.filter(proyecto=self.item.proyecto)).aggregate(total=Sum('costo_total'))
		return res['total']
	def unitario(self):
		return round(self.costo_total/self.cantidad,3)
		
class salidaMaterial(models.Model):
	almacen = models.ForeignKey(almacen)
	material = models.ForeignKey(material)
	confirmado = models.BooleanField(
		blank=False,
		null=False,
		default=False
	)
	item = models.ForeignKey('seguimiento.item')
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)

#insumos
class insumos(models.Model):
	decripcion = models.CharField(
		max_length=100,
		blank=False,
		null=False,
		unique=True
	)
	unidad = models.CharField(
		max_length=10,
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		null=True,
		blank=True,
	)
	def clean(self):
		aux = re.sub(' +',' ',self.decripcion)
		self.decripcion = aux.capitalize()
	def __str__(self):
		return self.decripcion
class insumosAlmacen(models.Model):
	almacen = models.ForeignKey(almacen)
	insumos = models.ForeignKey(insumos)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)
	class Meta:
		unique_together = (('almacen', 'insumos'),)
class ingresoInsumos(models.Model):
	almacen = models.ForeignKey(almacen)
	insumos = models.ForeignKey(insumos)
	proveedor = models.ForeignKey(proveedor)
	item = models.ForeignKey('seguimiento.item')
	no_factura = models.PositiveIntegerField(
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[0-9]{5,20}$', 
				message='El numero de factura tiene de 5 a 20 cifras', 
				code='Numero Invalido'
			)
		]
	)
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	costo_total = models.PositiveIntegerField(
		null=False,
		blank=False,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)
	def totalItem(self):
		res = ingresoInsumos.objects.filter(item=self.item).aggregate(total=Sum('costo_total'))
		return res['total']
	def total(self):
		item = apps.get_model('seguimiento', 'item')
		res = ingresoInsumos.objects.filter(item__in=item.objects.filter(proyecto=self.item.proyecto)).aggregate(total=Sum('costo_total'))
		return res['total']
	def unitario(self):
		return round(self.costo_total/self.cantidad,3)
		
class salidaInsumos(models.Model):
	almacen = models.ForeignKey(almacen)
	insumos = models.ForeignKey(insumos)
	item = models.ForeignKey('seguimiento.item')
	confirmado = models.BooleanField(
		blank=False,
		null=False,
		default=False
	)
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)

#herraminetas
class herramientas(models.Model):
	decripcion = models.CharField(
		max_length=100,
		blank=False,
		null=False,
		unique=True
	)
	tipo = models.CharField(
		max_length=30,
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		null=True,
		blank=True,
	)
	def clean(self):
		aux = re.sub(' +',' ',self.decripcion)
		self.decripcion = aux.capitalize()
	def __str__(self):
		return self.decripcion

class herramientasAlmacen(models.Model):
	almacen = models.ForeignKey(almacen)
	herramientas = models.ForeignKey(herramientas)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)
	def stock(self):
		return ingresoHerramientas.objects.filter(almacen=self.almacen,herramientas=self.herramientas).aggregate(total=Sum('cantidad'))['total']
	class Meta:
		unique_together = (('almacen', 'herramientas'),)

class ingresoHerramientas(models.Model):
	almacen = models.ForeignKey(almacen)
	herramientas = models.ForeignKey(herramientas)
	proveedor = models.ForeignKey(proveedor)
	no_factura = models.PositiveIntegerField(
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[0-9]{5,20}$', 
				message='El numero de factura tiene de 5 a 20 cifras', 
				code='Numero Invalido'
			)
		]
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	costo_total = models.PositiveIntegerField(
		null=False,
		blank=False,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)
	"""
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)
	"""

class salidaHerramientas(models.Model):
	almacen = models.ForeignKey(almacen)
	herramientas = models.ForeignKey(herramientas)
	item = models.ForeignKey('seguimiento.item')
	debuelto = models.BooleanField(
		blank=False,
		null=False,
		default=False
	)
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)
#maquinaria/equipo
class maquinaria_equipo(models.Model):
	decripcion = models.CharField(
		max_length=100,
		blank=False,
		null=False,
		unique=True
	)
	tipo = models.CharField(
		max_length=30,
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		null=True,
		blank=True,
	)
	def clean(self):
		aux = re.sub(' +',' ',self.decripcion)
		self.decripcion = aux.capitalize()
	def __str__(self):
		return self.decripcion

class maquinaria_equipoAlmacen(models.Model):
	almacen = models.ForeignKey(almacen)
	maquinaria_equipo = models.ForeignKey(maquinaria_equipo)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)
	def stock(self):
		return ingresoMaquinaria_equipo.objects.filter(almacen=self.almacen,maquinaria_equipo=self.maquinaria_equipo).aggregate(total=Sum('cantidad'))['total']
	class Meta:
		unique_together = (('almacen', 'maquinaria_equipo'),)

class ingresoMaquinaria_equipo(models.Model):
	almacen = models.ForeignKey(almacen)
	maquinaria_equipo = models.ForeignKey(maquinaria_equipo)
	proveedor = models.ForeignKey(proveedor)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	costo_total = models.PositiveIntegerField(
		null=False,
		blank=False,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)
	"""
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)
	"""

class salidaMaquinaria_equipo(models.Model):
	almacen = models.ForeignKey(almacen)
	maquinaria_equipo = models.ForeignKey(maquinaria_equipo)
	item = models.ForeignKey('seguimiento.item')
	debuelto = models.BooleanField(
		blank=False,
		null=False,
		default=False
	)
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)

class tipoActivo(models.Model):
	tipo = models.CharField(
		max_length=60,
		blank=False,
		null=False,
		unique=True
	)
	años_vida_util = models.PositiveIntegerField(
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		blank=True,
		null=True
	)
	def clean(self):
		aux = re.sub(' +',' ',self.tipo)
		self.tipo = aux.capitalize()
	def __str__(self):
		return self.tipo

class activo(models.Model):
	tipoActivo = models.ForeignKey(tipoActivo)
	descripcion = models.CharField(
		max_length=100,
		blank=False,
		null=False
	)
	marca = models.CharField(
		max_length=60,
		blank=False,
		null=False
	)
	modelo = models.CharField(
		max_length=60,
		blank=False,
		null=False
	)
	fecha_ingreso = models.DateField(
		blank=False,
		null=False
	)
	costo_total = models.FloatField(
		blank=False,
		null=False
	)
	def depreciasion(self):
		import datetime
		datenow = datetime.datetime.now()

		act = datenow.year - self.fecha_ingreso.year
		dep = self.costo_total / self.tipoActivo.años_vida_util

		tdep = dep*act
		res= self.costo_total-tdep

		return res
	def __str__(self):
		return self.descripcion