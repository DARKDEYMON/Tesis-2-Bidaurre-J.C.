from django.db import models

from django.core.exceptions import ValidationError,NON_FIELD_ERRORS
from django.core.validators import RegexValidator
from apps.almacenes.models import material, insumos, herramientas, maquinaria_equipo

from django.core.validators import MaxValueValidator, MinValueValidator

from django.utils.translation import ugettext_lazy as _

from django.db.models import F
from django.db.models import Sum
from django.db.models import Avg

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
	pocentaje_avance = models.PositiveIntegerField(
		null=False,
		blank=False,
		default=0
	)
	def __str__(self):
		return (self.objeto_de_la_contratacion)
	def clean(self):
		ini = self.fecha_inicio
		fin = self.plazo_previsto
		print("algo")
		print(ini)
		print(fin)
		if ini and fin and (fin<ini):
			raise ValidationError("El plazo previsto deve ser mayor al de la fecha de inicio")
	def save(self, *args, **kwargs):
		self.full_clean()
		return super(proyecto, self).save(*args, **kwargs)

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
	pocentaje_avance = models.PositiveIntegerField(
		null=False,
		blank=False,
		default=0
	)
	def __str__(self):
		return (self.proyecto.objeto_de_la_contratacion+':'+self.descripcion)
	def clean(self):
		#print(self)
		ini = self.fecha_inicio
		fin = self.plazo_finalizacion
		if ini and fin and (fin<ini):
			raise ValidationError("El plazo de finalisacion deve ser mayor al de la fecha de inicio")
	"""
		print(self)
		inip = self.proyecto.fecha_inicio
		finp = self.proyecto.plazo_previsto
		if (inip <= ini <= finp) and (inip <= fin <= finp):
			raise ValidationError("Las fechas no estas entre los plasos del proyecto")
		
	def save(self, *args, **kwargs):
		ini = self.fecha_inicio
		fin = self.plazo_finalizacion
		inip = self.proyecto.fecha_inicio
		finp = self.proyecto.plazo_previsto
		if (inip <= ini <= finp) and (inip <= fin <= finp):
			raise ValidationError("Las fechas no estas entre los plasos del proyecto")
	"""
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
		null=False,
		default=False
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
		null=False,
		default=False
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
		null=False,
		default=False
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
		null=False,
		default=False
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
	planificacion = models.BooleanField(
		blank=False,
		null=False,
		default=False
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
	planificacion = models.BooleanField(
		blank=False,
		null=False,
		default=False
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
	unidad =models.CharField(
		max_length=10,
		blank=False,
		null=False
	)
	planificacion = models.BooleanField(
		blank=False,
		null=False,
		default=False
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
		default = 1.0,
		validators=[MinValueValidator(0.0001,"El valor no puede ser cero")]
	)
	largo = models.FloatField(
		null = False,
		blank = False,
		default = 1.0,
		validators=[MinValueValidator(0.0001,"El valor no puede ser cero")]
	)
	ancho = models.FloatField(
		null = False,
		blank = False,
		default = 1.0,
		validators=[MinValueValidator(0.0001,"El valor no puede ser cero")]
	)
	observaciones = models.TextField(
		blank=True,
		null=True
	)
	def __str__(self):
		return (self.item.descripcion)
	def save(self, *args, **kwargs):
		super(reportes_avance, self).save(*args, **kwargs)
		unidad = self.item.unidad
		cantidad_total = self.item.cantidad
		print('tipo '+str(self.item.unidad))
		print('total '+str(self.item.cantidad))
		res=None;
		if (str(unidad) == 'Gbl'):
			res = reportes_avance.objects.filter(item=self.item).aggregate(total_avance=Sum('alto'))
			print('ubicado Gbl: '+str(res))
		if (str(unidad) == 'm2'):
			res = reportes_avance.objects.filter(item=self.item).aggregate(total_avance=Sum('alto')*Sum('largo'))
			print('ubicado m2: '+str(res))
		if (str(unidad) == 'm3'):
			res = reportes_avance.objects.filter(item=self.item).aggregate(total_avance=Sum('alto')*Sum('largo')*Sum('ancho'))
			print('ubicado m3: '+str(res))

		if (res!=None):
			porcen = (res['total_avance']/cantidad_total)*100
			itemg = item.objects.get(id=self.item.id);
			if(porcen>100):
				itemg.pocentaje_avance = 100
				itemg.save()
				print("porcen "+str(porcen))
			else:
				itemg.pocentaje_avance = int(porcen)
				itemg.save()
				print("porcen "+str(porcen))
			current_pro_porcent = item.objects.filter(proyecto=self.item.proyecto).aggregate(avance_grl=Avg('pocentaje_avance'))
			current_pro = proyecto.objects.get(id=self.item.proyecto.id)
			current_pro.pocentaje_avance = int(current_pro_porcent['avance_grl'])
			current_pro.save()
			print(current_pro_porcent)
	def delete(self, *args, **kwargs):
		super(reportes_avance, self).delete(*args, **kwargs)
		print("se borro algo"+str(self))
		unidad = self.item.unidad
		cantidad_total = self.item.cantidad
		print('tipo '+str(self.item.unidad))
		print('total '+str(self.item.cantidad))
		res=None;
		if (str(unidad) == 'Gbl'):
			res = reportes_avance.objects.filter(item=self.item).aggregate(total_avance=Sum('alto'))
			print('ubicado Gbl: '+str(res))
		if (str(unidad) == 'm2'):
			res = reportes_avance.objects.filter(item=self.item).aggregate(total_avance=Sum('alto')*Sum('largo'))
			print('ubicado m2: '+str(res))
		if (str(unidad) == 'm3'):
			res = reportes_avance.objects.filter(item=self.item).aggregate(total_avance=Sum('alto')*Sum('largo')*Sum('ancho'))
			print('ubicado m3: '+str(res))

		if (res!=None):
			porcen = (res['total_avance']/cantidad_total)*100
			itemg = item.objects.get(id=self.item.id);
			if(porcen>100):
				itemg.pocentaje_avance = 100
				itemg.save()
				print("porcen "+str(porcen))
			else:
				itemg.pocentaje_avance = int(porcen)
				itemg.save()
				print("porcen "+str(porcen))
			current_pro_porcent = item.objects.filter(proyecto=self.item.proyecto).aggregate(avance_grl=Avg('pocentaje_avance'))
			current_pro = proyecto.objects.get(id=self.item.proyecto.id)
			current_pro.pocentaje_avance = int(current_pro_porcent['avance_grl'])
			current_pro.save()
			print(current_pro_porcent)
		

def validate_file_extension(value):
	import os
	ext = os.path.splitext(value.name)[1]
	valid_extensions = ['.jpg','.png']
	if not ext in valid_extensions:
		raise ValidationError(u'Tipo de Archibo no Soportado!')
		
class reporte_fotografico(models.Model):
	reportes_avance = models.ForeignKey(reportes_avance)
	date = models.DateField(
		blank=False,
		null=False,
		auto_now=True
	)
	fotos_reporte = models.FileField(
		upload_to='reporte_fotos/', 
		validators=[validate_file_extension],
		null=True,
		blank=True
	)
	def __str__(self):
		return (self.reportes_avance.item.descripcion)