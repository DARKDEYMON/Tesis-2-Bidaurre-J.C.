from django.forms import ModelForm
from django import forms
from apps.personal.models import kardex

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.urls import reverse

class crearUsuarioKardexForm(ModelForm):
	class Meta:
		model = kardex
		"""
		fields = [
			'ci',
			'profecion',
			'telefono_fijo',
			'celular',
			'direccion',
			'nivel_de_confiabilidad',
			'curriculum',
		]
		"""
		exclude = ['user']
		widgets = {
			'ci':forms.TextInput(attrs={'class':'form-control'}),
			'profecion':forms.TextInput(attrs={'class':'form-control'}),
			'telefono_fijo':forms.TextInput(attrs={'class':'form-control'}),
			'celular':forms.TextInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),
			'nivel_de_confiabilidad':forms.Select(attrs={'class':'form-control'}),
			'curriculum':forms.FileInput(attrs={'class':'form-control','accept':'.pdf,.doc,.docx'}),
		}
class searchForm(forms.Form):
	search = forms.IntegerField(label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Busqueda por id...'}))

class addPermissionsFrom(forms.Form):
	mod_personal = forms.BooleanField(label='Dar permiso para el modulo de personal', required=False)
	mod_seguimiento = forms.BooleanField(label='Dar permiso para el modulo de Administracion de proyectos', required=False)
	mod_almacenes = forms.BooleanField(label='Dar permiso para el modulo de Administracion de almacenes', required=False)


class crearUsuarioUserForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	#email = forms.EmailField(required=True)
	class Meta:
		model=User
		fields=[
			'username',
			'password1',
			'password2',
			'first_name',
			'last_name',
			'email'
		]
		widgets = {
			'username':forms.TextInput(attrs={'class':'form-control'}),
			'password1':forms.PasswordInput(attrs={'class':'form-control'}),
			'password2':forms.PasswordInput(attrs={'class':'form-control'}),
			'first_name':forms.TextInput(attrs={'class':'form-control'}),
			'last_name':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(crearUsuarioUserForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = True
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
class crearModificarKardexForm(ModelForm):
	class Meta:
		model = kardex
		fields = [		
			'telefono_fijo',
			'celular',
			'direccion',
			'curriculum',
		]
		widgets = {
			'telefono_fijo':forms.TextInput(attrs={'class':'form-control'}),
			'celular':forms.TextInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),
			'curriculum':forms.FileInput(attrs={'class':'form-control','accept':'.pdf,.doc,.docx'}),
		}
class darBajaForm(ModelForm):
	class Meta:
		model = User
		fields = [
			'is_active'
		]