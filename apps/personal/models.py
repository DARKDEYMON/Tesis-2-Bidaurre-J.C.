from django.db import models
from django.contrib.auth.models import User

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
				regex=r'[a-zA-Z]+',
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
				message='El celular tiene un maximo de 8 dijitos', 
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
		blank=False
	)
	salario = models.FloatField(
		null=False,
		blank=False,
		validators=[MinValueValidator(1800,"El salario minimo nacional es 1800")]
	)
	encargado_de_reportes_avance = models.BooleanField(
		null=False,
		blank=False,
		default=False
	)
	def __str__(self):
		#return '{}{}'.format(self.nombre_cargo)
		return (self.nombre_cargo)

class designacion(models.Model):
	user = models.ForeignKey(User)
	cargo = models.ForeignKey(cargo)
	proyecto = models.ForeignKey(proyecto)
	def __str__(self):
		return (self.user.first_name)