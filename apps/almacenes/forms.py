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

class crearProveedorForm(ModelForm):
	class Meta:
		model = proveedor
		exclude = ['']

#material
class crearMaterialForm(ModelForm):
	class Meta:
		model = material
		exclude = ['']
		labels = {
			'tipo_item':'Tipo de Item',
		}

class crearIngresoMaterialForm(ModelForm):
	class Meta:
		model = ingresoMaterial
		exclude = ['almacen','item']

class crearSalidaMaterialForm(ModelForm):
	class Meta:
		model = salidaMaterial
		exclude = ['almacen','item']

#insumo
class crearIngresoInsumoForm(ModelForm):
	class Meta:
		model = ingresoInsumos
		exclude = ['almacen','item']

class crearSalidaInsumoForm(ModelForm):
	class Meta:
		model = salidaInsumos
		exclude = ['almacen','item']
#herramientas
class crearHerramientasForm(ModelForm):
	class Meta:
		model = herramientas
		exclude = ['']

CHOICES = (('1', 'ID'),('2', 'Nombre'),)
class searchForm(forms.Form):
	search = forms.IntegerField(label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Busqueda por...'}))
	buscar_por = forms.ChoiceField(label="", help_text="", choices=CHOICES)