from django.shortcuts import render
from apps.seguimiento.forms import *
from apps.seguimiento.models import *

# Create your views here. D:\Maritza-2012\PUNA-Proy Ecoturistico Thalaqocha\A-PROPUESTA\1-TDRs

from django.views.generic import ListView, CreateView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy

class crearProyecto(CreateView):
	form_class = crearProyectoForm
	template_name = 'seguimiento/nuevoproyecto.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')

class listaProyectos(CreateView,ListView):
	model = proyecto
	form_class = searchForm
	template_name = 'seguimiento/listaproyecto.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaProyectos, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))