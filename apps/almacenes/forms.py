from django.forms import ModelForm
from django import forms
from apps.almacenes.models import *

class crearItemAlmacenForm(ModelForm):
	class Meta:
		model = itemsAlmacen
		exclude = ['']
		labels = {
			'tipo_item':'Tipo de Item',
		}
class crearProveedorForm(ModelForm):
	class Meta:
		model = proveedor
		exclude = ['']