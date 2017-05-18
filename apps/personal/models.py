from django.db import models
from django.contrib.auth.models import User
from django.apps import apps

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from apps.seguimiento.models  import proyecto

from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# validador de extencion de archibos
def validate_file_extension(value):
	import os
	ext = os.path.splitext(value.name)[1]
	valid_extensions = ['.pdf','.doc','.docx']
	if not ext in valid_extensions:
		raise ValidationError(u'Tipo de Archibo no Soportado!')

class minnacional(models.Model):
	minimo_nacional = models.PositiveIntegerField(
		null=False,
		blank=False,
		validators=[MinValueValidator(1000,"El salario minimo en el pais actualmente no es por debajo de los 1000 Bs")]
	)
	actualisar_sueldos = models.BooleanField(
		null=False,
		blank=False,
		default=False
	)
	def save(self, *args, **kwargs):
		super(minnacional, self).save(*args, **kwargs)
		a = apps.get_model('personal', 'cargo')
		res = a.objects.all()
		mi = minnacional.objects.get(id=1)
		if mi.actualisar_sueldos:
			for b in res:
				if b.salario < mi.minimo_nacional:
					print('aqui')
					b.salario = mi.minimo_nacional
					b.save()
	def __str__(self):
		return str(self.minimo_nacional)
class kardex(models.Model):
	user = models.OneToOneField(User)
	ci = models.CharField(
		max_length=9, 
		null=False, 
		blank=False, 
		unique=True, 
		validators=[
			# validadores de filas
			RegexValidator(
				regex=r'[0-9]{7}[a-zA-Z]{0,2}', 
				message='El CI Tiene un Maximo de 7 Digitos y en algunos casos dos letras mas', 
				code='Numero Invalido'
			)
		]
	)
	profesion =models.CharField(
		max_length=40,
		null=False,
		blank=False,
		validators=[
			# validadores de filas
			RegexValidator(
				regex=r'^[a-zA-Z]{3,}$',
				message='La profecion deve contener solo letras', 
				code='Numero Invalido'
			)
		]
	)
	telefono_fijo = models.PositiveIntegerField(
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
	celular = models.PositiveIntegerField(
		null=False, 
		blank=False, 
		validators=[
			RegexValidator(
				regex=r'^[0-9]{8}$',
				message='El celular tiene 8 dijitos',
				code='Numero Invalido'
			)
		]
	)
	direccion = models.CharField(
		max_length=50,
		null=False,
		blank=False
	)
	nivel_de_confiabilidad = models.PositiveIntegerField(
		null=False, 
		blank=False, 
		default=0, 
		choices=((0,0),(1,1),(2,2),(3,3),(4,4),(5,5))
	)
	curriculum = models.FileField(
		upload_to='curriculums/', 
		validators=[validate_file_extension],
		null=True,
		blank=True
	)
	def __str__(self):
		#return '{}{}'.format(self.ci);
		return (self.ci);

class cargo(models.Model):
	nombre_cargo = models.CharField(
		max_length=60,
		null=False,
		blank=False,
		validators=[
			# validadores de filas
			RegexValidator(
				regex=r'^(([a-zA-Z]{2,} )||([a-zA-Z]{2,}))+$',
				message='El cargo deve contener solo letras y un minimo de dos caracteres',
				code='Numero Invalido'
			)
		]
	)
	salario = models.FloatField(
		null=False,
		blank=False,
		#validators=[MinValueValidator(minnacional.objects.get(id=1).minimo_nacional,"El salario minimo nacional es "+str(minnacional.objects.get(id=1)))]
	)
	encargado_de_reportes_avance = models.BooleanField(
		null=False,
		blank=False,
		default=False
	)
	def clean(self):
		if(self.salario<minnacional.objects.get(id=1).minimo_nacional):
			raise ValidationError("El salario minimo nacional es "+str(minnacional.objects.get(id=1)))
	def __str__(self):
		#return '{}{}'.format(self.nombre_cargo)
		return (self.nombre_cargo)

class designacion(models.Model):
	user = models.ForeignKey(User)
	cargo = models.ForeignKey(cargo)
	proyecto = models.ForeignKey(proyecto)
	def __str__(self):
		return (self.user.first_name)