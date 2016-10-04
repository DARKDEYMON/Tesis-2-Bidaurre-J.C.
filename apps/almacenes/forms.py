from django.forms import ModelForm
from django import forms
from apps.almacenes.models import *

class crearAlmacenForm(ModelForm):
	class Meta:
		model = almacen
		exclude = ['']

class actualisarAlmacenForm(ModelForm):
	class Meta:
		model = almacen
		exclude = ['ciudad']

class crearMaterialForm(ModelForm):
	class Meta:
		model = material
		exclude = ['']
		labels = {
			'tipo_item':'Tipo de Item',
		}

class crearProveedorForm(ModelForm):
	class Meta:
		model = proveedor
		exclude = ['']
class crearHerramientasForm(ModelForm):
	class Meta:
		model = herramientas
		exclude = ['']
#los buenos
class crearIngresoInsumoForm(ModelForm):
	class Meta:
		model = ingresoInsumos
		exclude = ['almacen','item']

class crearSalidaInsumoForm(ModelForm):
	class Meta:
		model = salidaInsumos
		exclude = ['almacen','item']

CHOICES = (('1', 'ID'),('2', 'Nombre'),)
class searchForm(forms.Form):
	search = forms.IntegerField(label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Busqueda por...'}))
	buscar_por = forms.ChoiceField(label="", help_text="", choices=CHOICES)