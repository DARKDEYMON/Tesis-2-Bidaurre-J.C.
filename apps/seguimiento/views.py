from django.shortcuts import render
from apps.seguimiento.forms import *

# Create your views here. D:\Maritza-2012\PUNA-Proy Ecoturistico Thalaqocha\A-PROPUESTA\1-TDRs

from django.views.generic import ListView, CreateView, UpdateView, FormView

class crearProyecto(CreateView):
	form_class = crearProyectoForm
	template_name = 'seguimiento/nuevoproyecto.html'
	succes_url = '/'