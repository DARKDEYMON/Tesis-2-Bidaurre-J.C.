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
			'fecha_inicio':Html5DateInput(),
			'plaso_previsto':Html5DateInput()
		}
		labels = {
			'ec_telefono':'Telefono de la entidad contratante',
			'ec_direccion':'Direccion dela entidad contratante',
			'ec_email':'Email de la entidad contratante'
		}
CHOICES = (('1', 'ID'),('2', 'Nombre'),)
class searchForm(forms.Form):
	search = forms.IntegerField(label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Busqueda por...'}))
	buscar_por = forms.ChoiceField(label="", help_text="", choices=CHOICES)