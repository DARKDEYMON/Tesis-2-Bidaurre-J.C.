from django.forms import ModelForm
from django import forms
from apps.almacenes.models import *

class Html5DateInput(forms.DateInput):
	input_type = 'date'

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
		labels = {
			'rason_social':'Razon social' 
		}

#material
class crearMaterialForm(ModelForm):
	class Meta:
		model = material
		exclude = ['']
		labels = {
			'tipo_item':'Tipo de Item',
			'decripcion':'Descripcion'
		}

class crearIngresoMaterialForm(ModelForm):
	class Meta:
		model = ingresoMaterial
		exclude = ['almacen','item']

class crearSalidaMaterialForm(ModelForm):
	class Meta:
		model = salidaMaterial
		exclude = ['almacen','item','confirmado']

#insumo
class crearInsumoForm(ModelForm):
	class Meta:
		model = insumos
		exclude = ['']
		labels = {
			'decripcion':'Descripcion'
		}

class crearIngresoInsumoForm(ModelForm):
	class Meta:
		model = ingresoInsumos
		exclude = ['almacen','item']

class crearSalidaInsumoForm(ModelForm):
	class Meta:
		model = salidaInsumos
		exclude = ['almacen','item','confirmado']
#herramientas
class crearHerramientasForm(ModelForm):
	class Meta:
		model = herramientas
		exclude = ['']
		labels = {
			'decripcion':'Descripcion'
		}

class crearIngresoHerramientasForm(ModelForm):
	class Meta:
		model = ingresoHerramientas
		exclude = ['almacen']

class crearSalidaHerramientasForm(ModelForm):
	class Meta:
		model = salidaHerramientas
		exclude = ['almacen','item','debuelto']
		labels = {
			'debuelto':'Devuelto'
		}

class crearMaquinariaEquipoForm(ModelForm):
	class Meta:
		model = maquinaria_equipo
		exclude = ['']

class crearIngresoMaquinariaEquipoForm(ModelForm):
	class Meta:
		model = ingresoMaquinaria_equipo
		exclude = ['almacen']

class crearSalidaMaquinariaEquipoForm(ModelForm):
	class Meta:
		model = salidaMaquinaria_equipo
		exclude = ['almacen','item','debuelto']
		labels = {
			'debuelto':'Devuelto'
		}

CHOICES = (('1', 'ID'),('2', 'Nombre'),)
class searchForm(forms.Form):
	search = forms.IntegerField(label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Busqueda por...'}))
	buscar_por = forms.ChoiceField(label="", help_text="", choices=CHOICES)

class crearDebolucionHerramientas(ModelForm):
	class Meta:
		model = salidaHerramientas
		fields = ['debuelto']
		labels = {
			'debuelto':'Devuelto'
		}

class crearDebolucionMaquinariaEquipo(ModelForm):
	class Meta:
		model = salidaMaquinaria_equipo
		fields = ['debuelto']
		labels = {
			'debuelto':'Devuelto'
		}

class crearTipoActivoForm(ModelForm):
	class Meta:
		model = tipoActivo
		exclude = ['']
		
class crearActivoForm(ModelForm):
	class Meta:
		model = activo
		exclude = ['']
		widgets = {
			'fecha_ingreso':Html5DateInput(format=('%Y-%m-%d')),
		}