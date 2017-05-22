from django.forms import ModelForm
from django import forms
from apps.seguimiento.models import *

#witdget para html5
class Html5DateInput(forms.DateInput):
	input_type = 'date'

class crearProyectoForm(ModelForm):
	class Meta:
		model = proyecto
		exclude = ['pocentaje_avance']
		widgets = {
			'fecha_inicio':Html5DateInput(format=('%Y-%m-%d')),#attrs={'format':'dd/MM/yyyy'}),
			'plazo_previsto':Html5DateInput(format=('%Y-%m-%d'))
		}
		labels = {
			'ec_telefono':'Telefono de la entidad contratante',
			'ec_direccion':'Direccion de la entidad contratante',
			'ec_email':'Email de la entidad contratante'
		}


class crearItemsForm(ModelForm):
	class Meta:
		model = item
		exclude =['proyecto','pocentaje_avance']
		widgets = {
			'fecha_inicio':Html5DateInput(format=('%Y-%m-%d')),
			'plazo_finalizacion':Html5DateInput(format=('%Y-%m-%d'))
		}
		labels = {
			'plazo_finalizacion':'Plazo de finalizacion',
		}

CHOICES = (('1', 'ID'),('2', 'Nombre'),)
class searchForm(forms.Form):
	search = forms.IntegerField(label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Busqueda por...'}))
	buscar_por = forms.ChoiceField(label="", help_text="", choices=CHOICES)


class crearPeticionMaterialForm(ModelForm):
	"""
	def __init__(self,*args,**kwargs):
		super (crearPeticionMaterialForm,self ).__init__(*args,**kwargs) # populates the post
		self.fields['itemsAlmacen'].queryset = itemsAlmacen.objects.filter(tipo_item='MA')
	"""
	class Meta:
		model = peticion_materiales
		exclude = ['item']
		#marcado de cambio verificar
		labels = {
			'petion_de_planificacion':'Peticion de planificacion',
		}

class crearPeticionInsumosForm(ModelForm):
	class Meta:
		model = peticion_insumos
		exclude = ['item']
		labels = {
			'petion_de_planificacion':'Peticion de planificacion',
		}


class crearPeticionHerramientas(ModelForm):
	class Meta:
		model = peticion_Herramientas
		exclude = ['item']
		labels = {
			'petion_de_planificacion':'Peticion de planificacion',
		}

class crearPeticionMaqHeq(ModelForm):
	class Meta:
		model = peticion_maquinaria_equipo
		exclude = ['item']

class crearRequerimientoPersonalForm(ModelForm):
	class Meta:
		model = requerimiento_personal
		exclude = ['item']

class crearRequerimientoMaHeForm(ModelForm):
	class Meta:
		model = requerimiento_maq_he
		exclude = ['item']
		labels = {
				'nombre_maq_he':'Nombre de la Maquinaria/Hequipo',
		}

class crearRequerimientoMaterialLocalForm(ModelForm):
	class Meta:
		model = materiales_locales
		exclude = ['item']

class crearReportesAvanceForm(ModelForm):
	class Meta:
		model = reportes_avance
		exclude = ['item']

class crearFotosReporteForm(ModelForm):
	class Meta:
		model = reporte_fotografico
		exclude = ['reportes_avance']