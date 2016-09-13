from django.db import models

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

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