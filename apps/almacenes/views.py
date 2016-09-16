from django.shortcuts import render
from apps.almacenes.forms import *

# Create your views here.

from django.views.generic import ListView, CreateView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy

class crearItemAlmacen(CreateView):
	form_class = crearItemAlmacenForm
	template_name = 'almacen/nuevoitemalmacen.html'
	success_url = '/'

class crearProveedor(CreateView):
	form_class = crearProveedorForm
	template_name = 'almacen/nuevoproveedor.html'
	success_url = '/'