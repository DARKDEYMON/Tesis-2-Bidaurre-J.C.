from django.db import models
from django.apps import apps

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
		blank=False,
		validators=[MinValueValidator(10000,"El presupuesto minimo de un proyecto esta por ensima de los 10000")]
	)
	pocentaje_avance = models.PositiveIntegerField(
		null=False,
		blank=False,
		default=0
	)
	def __str__(self):
		return (self.objeto_de_la_contratacion)

	def tMaterialPla(self):
		return self.item_set.all()[0].peticion_materiales_set.all()[0].total()
	def tMaterialEjec(self):
		return self.item_set.all()[0].ingresomaterial_set.all()[0].total()
	def resEjecMaterial(self):
		if (not self.tMaterialPla() == None and not self.tMaterialEjec() == None):
			return (self.tMaterialPla() - self.tMaterialEjec())
		return None

	def tInsumosPla(self):
		return self.item_set.all()[0].peticion_insumos_set.all()[0].total()
	def tInsumosEjec(self):
		return self.item_set.all()[0].ingresoinsumos_set.all()[0].total()
	def resEjecInsumos(self):
		if (not self.tInsumosPla() == None and not self.tInsumosEjec() == None):
			return (self.tInsumosPla() - self.tInsumosEjec())
		return None

	def tPersonalEjec(self):
		return self.item_set.all()[0].requerimiento_personal_set.all()[0].total()

	def tMaqEqEjec(self):
		return self.item_set.all()[0].requerimiento_maq_he_set.all()[0].total()

	def tMatLocEjec(self):
		return self.item_set.all()[0].materiales_locales_set.all()[0].total()

	def totalSueldo(self):
		n = (self.plazo_previsto.year - self.fecha_inicio.year)*12 + self.plazo_previsto.month - self.fecha_inicio.month
		if n== 0:
			n=1
		cargo = apps.get_model('personal', 'cargo')
		designacion = apps.get_model('personal', 'designacion')
		res = cargo.objects.filter(id__in=designacion.objects.filter(proyecto=proyecto.objects.get(id=self.id))).aggregate(sueldos=Sum('salario'))
		return res['sueldos'] * n+1
	def clean(self):
		ini = self.fecha_inicio
		fin = self.plazo_previsto
		#print("algo")
		#print(ini)
		#print(fin)
		if ini and fin and (fin<ini):
			raise ValidationError("El plazo previsto deve ser mayor al de la fecha de inicio")
	def enTiempo(self):
		import datetime
		n = datetime.datetime.now().date()
		if (self.fecha_inicio <= n <= self.plazo_previsto) or (self.pocentaje_avance>=100):
			return True
		else:
			return False
	def save(self, *args, **kwargs):
		self.full_clean()
		return super(proyecto, self).save(*args, **kwargs)
	class Meta:
		ordering = ['pk']

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
	def enTiempo(self):
		import datetime
		n = datetime.datetime.now().date()
		if (self.fecha_inicio <= n <= self.plazo_finalizacion) or (self.pocentaje_avance>=100):
			return True
		else:
			return False
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
		ordering = ['pk']
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
	def totalItem(self):
		res = peticion_materiales.objects.filter(item=self.item).aggregate(total=Sum('precio_estimado_total'))
		return res['total']
	def total(self):
		res = peticion_materiales.objects.filter(item__in=item.objects.filter(proyecto=self.item.proyecto)).aggregate(total=Sum('precio_estimado_total'))
		return res['total']
	def __str__(self):
		return (self.material.decripcion)
	class Meta:
		ordering = ['pk']

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
	def totalItem(self):
		res = peticion_insumos.objects.filter(item=self.item).aggregate(total=Sum('precio_estimado_total'))
		return res['total']
	def total(self):
		res = peticion_insumos.objects.filter(item__in=item.objects.filter(proyecto=self.item.proyecto)).aggregate(total=Sum('precio_estimado_total'))
		return res['total']
	def __str__(self):
		return (self.insumos.decripcion)
	class Meta:
		ordering = ['pk']

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
	class Meta:
		ordering = ['pk']

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
	class Meta:
		ordering = ['pk']
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
	def totalItem(self):
		res = requerimiento_personal.objects.filter(item=self.item).aggregate(total=Sum('precio_total'))
		return res['total']
	def total(self):
		res = requerimiento_personal.objects.filter(item__in=item.objects.filter(proyecto=self.item.proyecto)).aggregate(total=Sum('precio_total'))
		return res['total']
	def __str__(self):
		return (self.funcion)
	class Meta:
		ordering = ['pk']

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
	def totalItem(self):
		res = requerimiento_maq_he.objects.filter(item=self.item).aggregate(total=Sum('precio_total'))
		return res['total']
	def total(self):
		res = requerimiento_maq_he.objects.filter(item__in=item.objects.filter(proyecto=self.item.proyecto)).aggregate(total=Sum('precio_total'))
		return res['total']
	def __str__(self):
		return (self.nombre_maq_he)
	class Meta:
		ordering = ['pk']

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
	def totalItem(self):
		res = materiales_locales.objects.filter(item=self.item).aggregate(total=Sum('precio_total'))
		return res['total']
	def total(self):
		res = materiales_locales.objects.filter(item__in=item.objects.filter(proyecto=self.item.proyecto)).aggregate(total=Sum('precio_total'))
		return res['total']
	def __str__(self):
		return (self.descripcion)
	class Meta:
		ordering = ['pk']
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
	class Meta:
		ordering = ['pk']

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
	class Meta:
		ordering = ['pk']