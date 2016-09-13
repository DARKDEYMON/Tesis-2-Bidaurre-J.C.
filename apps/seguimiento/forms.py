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