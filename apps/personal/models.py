from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
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
	profecion =models.CharField(
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
		validators=[validate_file_extension]
	)
	def __str__(self):
		return '{}{}'.format(self.ci);

class cargo(models.Model):
	codigo_cargo = models.CharField(
		max_length = 4,
		null=False,
		blank=False,
		unique=True,
		validators=[
			RegexValidator(
				regex=r'^[0-9A-Z]{4}$', 
				message='El codigo de cargo es de cuatro caracteres y no contiene simbolos especiales', 
				code='Numero Invalido'
			)
		]
	)
	nombre_cargo = models.CharField(
		max_length=60,
		null=False,
		blank=False
	)
	salario = models.FloatField(
		null=False,
		blank=False
	)
	def __str__(self):
		return '{}{}'.format(self.nombre_cargo)