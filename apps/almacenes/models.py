from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.core.validators import RegexValidator

# Create your models here.

class itemsAlmacen(models.Model):
	decripcion = models.CharField(
		max_length=100,
		blank=False,
		null=False
	)
	tipo_item = models.CharField(
		max_length=2,
		blank=False,
		null=False
	)
	cantidad = models.IntegerField(
		blank=False,
		null=False,
		choices=(('MA','Material'),('He','Herramienta'),('EQ','Equipo'),('IN','Insumo'))
	)
	unidad = models.CharField(
		max_length=10,
		blank=False,
		null=False
	)
	class Meta:
		verbose_name = _('item Almacen')
		verbose_name_plural = _('items Almacen')

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
	class Meta:
		verbose_name_plural = _('proveedores')