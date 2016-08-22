from django.forms import ModelForm
from django import forms
from apps.personal.models import kardex

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
			'curriculum':forms.FileInput(attrs={'class':'form-control'}),
		}
class searchForm(forms.Form):
	search = forms.IntegerField(label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Busqueda por id...'}))
			

class crearUsuarioUserForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
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