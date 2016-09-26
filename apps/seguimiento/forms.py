from django.forms import ModelForm
from django import forms
from apps.seguimiento.models import *

#witdget para html5
class Html5DateInput(forms.DateInput):
	input_type = 'date'

class crearProyectoForm(ModelForm):
	class Meta:
		model = proyecto
		exclude = ['']
		widgets = {
			'fecha_inicio':Html5DateInput(format=('%Y-%m-%d')),#attrs={'format':'dd/MM/yyyy'}),
			'plaso_previsto':Html5DateInput(format=('%Y-%m-%d'))
		}
		labels = {
			'ec_telefono':'Telefono de la entidad contratante',
			'ec_direccion':'Direccion de la entidad contratante',
			'ec_email':'Email de la entidad contratante'
		}

class crearItemsForm(ModelForm):
	class Meta:
		model = item
		exclude =['proyecto']
		widgets = {
			'fecha_inicio':Html5DateInput(),
			'plaso_finalisacion':Html5DateInput()
		}
		labels = {
			'plaso_finalisacion':'Plazo de Finalisacion',
		}

CHOICES = (('1', 'ID'),('2', 'Nombre'),)
class searchForm(forms.Form):
	search = forms.IntegerField(label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Busqueda por...'}))
	buscar_por = forms.ChoiceField(label="", help_text="", choices=CHOICES)