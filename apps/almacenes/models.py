from django.db import models
from django.utils.translation import ugettext_lazy as _
#from apps.seguimiento.models import item

from django.core.validators import RegexValidator

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
	def __str__(self):
		return self.ciudad

class proveedor(models.Model):
	rason_social = models.CharField(
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
		null=False
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
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	costo_total = models.PositiveIntegerField(
		null=False,
		blank=False
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)
class salidaMaterial(models.Model):
	almacen = models.ForeignKey(almacen)
	material = models.ForeignKey(material)
	item = models.ForeignKey('seguimiento.item')
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)

#insumos
class insumos(models.Model):
	decripcion = models.CharField(
		max_length=100,
		blank=False,
		null=False
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
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	costo_total = models.PositiveIntegerField(
		null=False,
		blank=False
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)
class salidaInsumos(models.Model):
	almacen = models.ForeignKey(almacen)
	insumos = models.ForeignKey(insumos)
	item = models.ForeignKey('seguimiento.item')
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)

#herraminetas
class herramientas(models.Model):
	decripcion = models.CharField(
		max_length=100,
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		null=True,
		blank=True,
	)
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
	class Meta:
		unique_together = (('almacen', 'herramientas'),)

class ingresoHerramientas(models.Model):
	almacen = models.ForeignKey(almacen)
	herramientas = models.ForeignKey(herramientas)
	proveedor = models.ForeignKey(proveedor)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	costo_total = models.PositiveIntegerField(
		null=False,
		blank=False
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)

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
		default=0
	)
#maquinaria/equipo
class maquinaria_equipo(models.Model):
	decripcion = models.CharField(
		max_length=100,
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		null=True,
		blank=True,
	)
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
	class Meta:
		unique_together = (('almacen', 'maquinaria_equipo'),)

class ingresoMaquinaria_equipo(models.Model):
	almacen = models.ForeignKey(almacen)
	maquinaria_equipo = models.ForeignKey(maquinaria_equipo)
	proveedor = models.ForeignKey(proveedor)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	costo_total = models.PositiveIntegerField(
		null=False,
		blank=False
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)

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
		default=0
	)