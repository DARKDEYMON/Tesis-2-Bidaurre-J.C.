from django.shortcuts import render
from apps.seguimiento.forms import *
from apps.seguimiento.models import *
from apps.personal.models import designacion

from django.http import HttpResponseRedirect, Http404
from django.http import JsonResponse


# Create your views here. D:\Maritza-2012\PUNA-Proy Ecoturistico Thalaqocha\A-PROPUESTA\1-TDRs

from django.views.generic import ListView, CreateView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy

#pdf
"""
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from django.http import HttpResponse

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus import Table,TableStyle
from reportlab.lib import colors
"""
from easy_pdf.views import PDFTemplateView

# crear proyecto
class crearProyecto(CreateView):
	form_class = crearProyectoForm
	template_name = 'seguimiento/nuevoproyecto.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')

class updateProyecto(UpdateView):
	model = proyecto
	form_class = crearProyectoForm
	template_name = 'seguimiento/nuevoproyecto.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')

# lista proyectos
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
	def get_queryset(self):
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id)
		else:
			object_list = self.model.objects.all().order_by('id')
		return object_list
# crea un item para un proyecto en especifico
class crearItem(CreateView):
	model_pk = proyecto
	form_class = crearItemsForm
	template_name = 'seguimiento/nuevoitem.html'
	success_url = 'seguimiento:listaitems'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		#pk1=self.kwargs['pk']
		#proyectoval = self.model_pk.objects.get(id=pk1)
		if form.is_valid():
			pk1=self.kwargs['pk']

			dat = self.model_pk.objects.get(id=pk1)
			ini = form.cleaned_data['fecha_inicio']
			fin = form.cleaned_data['plazo_finalizacion']
			inip = dat.fecha_inicio
			finp = dat.plazo_previsto
			"""
			print(ini)
			print(fin)
			print(inip)
			print(finp)
			print(inip <= ini <= finp)
			print(inip <= fin <= finp)
			print(not((inip <= ini <= finp) and (inip <= fin <= finp)))
			return
			"""
			if (not((inip <= ini <= finp) and (inip <= fin <= finp))):
				return self.render_to_response(self.get_context_data(form=form,error='Las fechas no estas entre los plasos del proyecto'))

			#pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.proyecto = self.model_pk.objects.get(id=pk1)
			form.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': pk1}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class updateItem(UpdateView):
	model =item
	form_class = crearItemsForm
	template_name = 'seguimiento/nuevoitem.html'
	success_url = 'seguimiento:listaitems'
	def get_success_url(self):
		return reverse_lazy(self.success_url, kwargs = {'pk': self.get_object().proyecto.pk})

# lista los items de un proyecto en espesifico
class listaItems(CreateView,ListView):
	model = item
	form_class = searchForm
	template_name = 'seguimiento/listaitems.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaItems, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			context['form'] = self.form_class()
			context['pk1'] = pk1
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id, proyecto = pk1)
		else:
			object_list = self.model.objects.filter(proyecto = pk1).order_by('id')
		return object_list

class listaPersonalProyecto(CreateView,ListView):
	model = designacion
	form_class = searchForm
	template_name = 'seguimiento/listapersonalpro.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaPersonalProyecto, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(proyecto = proyecto.objects.filter(id=pk1), id = id)
		else:
			object_list = self.model.objects.filter(proyecto = proyecto.objects.filter(id=pk1)).order_by('id')
		return object_list

class peticionMaterial(CreateView):
	model_pk = item
	form_class = crearPeticionMaterialForm
	template_name = 'seguimiento/peticionmaterial.html'
	success_url = 'seguimiento:listaitems'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': self.model_pk.objects.get(id=pk1).proyecto.id}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class updatePeticionMaterial(UpdateView):
	model = peticion_materiales
	form_class = crearPeticionMaterialForm
	template_name = 'seguimiento/peticionmaterial.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')
	def get_context_data(self, **kwargs):
		context = super (updatePeticionMaterial, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			ins = self.model.objects.get(pk=pk1)
			#print(datetime.datetime.strptime(str(ins.fecha_inicio), '%Y-%m-%d').strftime('%d-%m-%Y'))
			context['form'] = self.form_class(instance=ins)
		return context

class listaPeticionMaterial(CreateView,ListView):
	model = peticion_materiales
	form_class = searchForm
	template_name = 'seguimiento/listamaterialalmacen.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaPeticionMaterial, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1), id = id)
		else:
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1)).order_by('id')
		return object_list

class peticionInsumos(CreateView):
	model_pk = item
	form_class = crearPeticionInsumosForm
	template_name = 'seguimiento/peticioninsumos.html'
	success_url = 'seguimiento:listaitems'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': self.model_pk.objects.get(id=pk1).proyecto.id}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class updatePeticionInsumos(UpdateView):
	model = peticion_insumos
	form_class = crearPeticionInsumosForm
	template_name = 'seguimiento/peticioninsumos.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')
	def get_context_data(self, **kwargs):
		context = super (updatePeticionInsumos, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			ins = self.model.objects.get(pk=pk1)
			#print(datetime.datetime.strptime(str(ins.fecha_inicio), '%Y-%m-%d').strftime('%d-%m-%Y'))
			context['form'] = self.form_class(instance=ins)
		return context

class listaPeticionInsumos(CreateView,ListView):
	model = peticion_insumos
	form_class = searchForm
	template_name = 'seguimiento/listainsumosalmacen.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaPeticionInsumos, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1), id = id)
		else:
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1)).order_by('id')
		return object_list

class requerimientoPersonal(CreateView):
	model_pk = item
	form_class = crearRequerimientoPersonalForm
	template_name = 'seguimiento/requerimientopersonal.html'
	success_url = 'seguimiento:listaitems'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': self.model_pk.objects.get(id=pk1).proyecto.id}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class updateRequerimientoPersonal(UpdateView):
	model = requerimiento_personal
	form_class = crearRequerimientoPersonalForm
	template_name = 'seguimiento/requerimientopersonal.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')
	def get_context_data(self, **kwargs):
		context = super (updateRequerimientoPersonal, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			ins = self.model.objects.get(pk=pk1)
			#print(datetime.datetime.strptime(str(ins.fecha_inicio), '%Y-%m-%d').strftime('%d-%m-%Y'))
			context['form'] = self.form_class(instance=ins)
		return context

class listaRequerimientoPersonal(CreateView,ListView):
	model = requerimiento_personal
	form_class = searchForm
	template_name = 'seguimiento/listarequerimientopersonal.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaRequerimientoPersonal, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1), id = id)
		else:
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1)).order_by('id')
		return object_list

class requerimientoMaHe(CreateView):
	model_pk = item
	form_class = crearRequerimientoMaHeForm
	template_name = 'seguimiento/requerimientomahe.html'
	success_url = 'seguimiento:listaitems'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': self.model_pk.objects.get(id=pk1).proyecto.id}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class updateRequerimientoMaHe(UpdateView):
	model = requerimiento_maq_he
	form_class = crearRequerimientoMaHeForm
	template_name = 'seguimiento/requerimientomahe.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')
	def get_context_data(self, **kwargs):
		context = super (updateRequerimientoMaHe, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			ins = self.model.objects.get(pk=pk1)
			#print(datetime.datetime.strptime(str(ins.fecha_inicio), '%Y-%m-%d').strftime('%d-%m-%Y'))
			context['form'] = self.form_class(instance=ins)
		return context

class listaRequerimientoMaHe(CreateView,ListView):
	model = requerimiento_maq_he
	form_class = searchForm
	template_name = 'seguimiento/listaRequerimientomahe.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaRequerimientoMaHe, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1), id = id)
		else:
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1)).order_by('id')
		return object_list

class requerimientoMaterialesLocales(CreateView):
	model_pk = item
	form_class = crearRequerimientoMaterialLocalForm
	template_name = 'seguimiento/requerimientomaterlocal.html'
	success_url = 'seguimiento:listaitems'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': self.model_pk.objects.get(id=pk1).proyecto.id}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class updateRequerimientoMaterialesLocales(UpdateView):
	model = materiales_locales
	form_class = crearRequerimientoMaterialLocalForm
	template_name = 'seguimiento/requerimientomaterlocal.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')
	def get_context_data(self, **kwargs):
		context = super (updateRequerimientoMaterialesLocales, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			ins = self.model.objects.get(pk=pk1)
			#print(datetime.datetime.strptime(str(ins.fecha_inicio), '%Y-%m-%d').strftime('%d-%m-%Y'))
			context['form'] = self.form_class(instance=ins)
		return context

class listaRequerimientoMaterialeLocales(CreateView,ListView):
	model = materiales_locales
	form_class = searchForm
	template_name = 'seguimiento/listaRequerimientomaterialelocales.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaRequerimientoMaterialeLocales, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1), id = id)
		else:
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1)).order_by('id')
		return object_list


class requerimientoHerramientas(CreateView):
	model_pk = item
	form_class = crearPeticionHerramientas
	template_name = 'seguimiento/requerimientoherramientas.html'
	success_url = 'seguimiento:listaitems'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': self.model_pk.objects.get(id=pk1).proyecto.id}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class updatePeticionHerramientas(UpdateView):
	model = peticion_Herramientas
	form_class = crearPeticionHerramientas
	template_name = 'seguimiento/requerimientoherramientas.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')
	def get_context_data(self, **kwargs):
		context = super (updatePeticionHerramientas, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			ins = self.model.objects.get(pk=pk1)
			#print(datetime.datetime.strptime(str(ins.fecha_inicio), '%Y-%m-%d').strftime('%d-%m-%Y'))
			context['form'] = self.form_class(instance=ins)
		return context

class listaRequerimientoHerramientas(CreateView,ListView):
	model = peticion_Herramientas
	form_class = searchForm
	template_name = 'seguimiento/listapeticionherramientas.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaRequerimientoHerramientas, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1), id = id)
		else:
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1)).order_by('id')
		return object_list

class crearInforme(CreateView):
	model_pk = item
	form_class = crearReportesAvanceForm
	template_name = 'seguimiento/crearinforme.html'
	success_url = 'seguimiento:informefotografico'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			pk1=self.kwargs['pk']
			form = form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.save()
			#print (form)
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': form.pk }))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class updateCrearInforme(UpdateView):
	model = reportes_avance
	form_class = crearReportesAvanceForm
	template_name = 'seguimiento/crearinforme.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')
	def get_context_data(self, **kwargs):
		context = super (updateCrearInforme, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			ins = self.model.objects.get(pk=pk1)
			#print(datetime.datetime.strptime(str(ins.fecha_inicio), '%Y-%m-%d').strftime('%d-%m-%Y'))
			context['form'] = self.form_class(instance=ins)
		return context

class crearInformeFotografico(CreateView):
	model_pk = reportes_avance
	form_class = crearFotosReporteForm
	template_name = 'seguimiento/crearinformefotografico.html'
	success_url = 'seguimiento:informefotografico'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST,request.FILES)
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.reportes_avance = self.model_pk.objects.get(id=pk1)
			form.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': pk1 }))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class listaInformes(CreateView,ListView):
	model = reportes_avance
	form_class = searchForm
	template_name = 'seguimiento/listapeInformes.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaInformes, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1), id = id)
		else:
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1)).order_by('id')
		return object_list

class listaInformesFotos(ListView):
	model = reporte_fotografico
	template_name = 'seguimiento/listainformefotos.html'
	paginate_by = 10

	def get_queryset(self):
		pk1=self.kwargs['pk']
		print(pk1)
		object_list = self.model.objects.filter(reportes_avance = reportes_avance.objects.filter(id=pk1))
		return object_list

def calendar_proyecto(request,pk):
	import json
	dat = []

	query1 = item.objects.filter(proyecto__id=pk)
	if(len(query1)==0):
		return render (request,"seguimiento/calendar.html",{"error":"no existen items aun !!!!!"})
	query2 = query1[0].proyecto
	"""
	print(query1)
	for r in query1:
		res = {}
		res['title'] = r.descripcion
		res['start'] = str(r.fecha_inicio)
		res['end'] = str(r.plazo_finalizacion)
		dat.append(res)
	print(dat)
	"""
	return render (request,"seguimiento/calendar.html",{"pk":pk,"res":query1,"pro":query2})


class reporteProyecto(PDFTemplateView):
	template_name = "seguimiento/seguimiento_reporte.html"
	def get_context_data(self, **kwargs):
		context = super(reporteProyecto, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk')
		#print(pk)
		try:
			context['res'] = proyecto.objects.get(id=pk)
		except:
			raise Http404
		return context
class reporteProyectosEstado(PDFTemplateView):
	template_name = "seguimiento/rep_estadodeproyectos.html"
	def get_context_data(self, **kwargs):
		context = super(reporteProyectosEstado, self).get_context_data(**kwargs)
		#print(pk)
		try:
			context['res'] = proyecto.objects.all()
		except:
			raise Http404
		return context
"""
def reporteProyecto(request,pk):
	#consultas

	pro_ac = proyecto.objects.get(id=pk)

	y,x=A4
	#construccion
	response = HttpResponse(content_type='application/pdf')
	#response['Content-Disposition'] = 'attachment; filename=reporte.pdf'
	response['Content-Disposition'] = 'filename=reporte.pdf'
	#response["Content-Disposition"] = "inline"
	buffer = BytesIO()

	c = canvas.Canvas(buffer,pagesize=A4)
	comienso = 750
	print(A4)
	#encavesado espacio abajo arriba 91
	c.setLineWidth(.3)
	c.setFont('Helvetica',22)
	c.drawCentredString(y/2,comienso,'Reporte de proyecto')

	c.setFont('Helvetica',15)
	comienso=comienso-18
	c.drawString(30,comienso,'1. Informacion General.-')

	c.setFont('Helvetica',10)
	comienso=comienso-22
	c.drawString(30,comienso,'Objeto de la contratacion: '+pro_ac.objeto_de_la_contratacion)
	c.drawString(y/2,comienso,'Fecha de inicio: '+str(pro_ac.fecha_inicio))
	comienso=comienso-13
	c.drawString(30,comienso,'Modalidad de contratacion: '+pro_ac.modalidad_de_contratacion)
	c.drawString(y/2,comienso,'Plazo previsto de finalisacion: '+str(pro_ac.plazo_previsto))
	comienso=comienso-13
	c.drawString(30,comienso,'Entidad contratante: '+pro_ac.entidad_contratante)
	c.drawString(y/2,comienso,'Uvicacion: '+str(pro_ac.ubicacion_proyecto))
	comienso=comienso-13
	c.drawString(30,comienso,'Telefono de la entidad contratante: '+str(pro_ac.ec_telefono))
	c.drawString(y/2,comienso,'Presupuesto final: '+str(pro_ac.presupuesto_final))
	comienso=comienso-13
	c.drawString(30,comienso,'Direccion de la entidad contratante: '+str(pro_ac.ec_direccion))
	c.drawString(y/2,comienso,'porcentaje de avance: '+str(pro_ac.pocentaje_avance)+"%")
	comienso=comienso-13
	c.drawString(30,comienso,'Email de la entidad contratante: '+str(pro_ac.ec_email))

	#comienso=comienso-13
	#c.line(30,comienso,y-30,comienso)

	c.setFont('Helvetica',15)
	comienso=comienso-20
	c.drawString(30,comienso,'2. Informacion de Items.-')

	#items
	c.setFont('Helvetica',10)
	comienso=comienso-22
	items = pro_ac.item_set.all()

	for i in items:
		comienso=comienso-20
		c.setFont('Helvetica',15)
		c.drawString(30,comienso,'Descripcion de Item: '+str(i.descripcion))
		comienso=comienso-13
		c.setFont('Helvetica',10)
		c.drawString(30,comienso,'Fecha de inicio: '+str(i.fecha_inicio))
		comienso=comienso-13
		c.drawString(30,comienso,'Plazo de finalizacion: '+str(i.plazo_finalizacion))
		comienso=comienso-13
		c.drawString(30,comienso,'Unidad: '+str(i.unidad))
		comienso=comienso-13
		c.drawString(30,comienso,'Cantidad: '+str(i.cantidad))
		comienso=comienso-13
		c.drawString(30,comienso,'Porcentaje de avance: '+str(i.pocentaje_avance)+"%")
		comienso=comienso-13

		
		#if comienso<=300:
		#	print("ya")
		#	c.showPage()
		#	comienso = 750
		

		re = i.reportes_avance_set.all()

		for r in re:
			comienso=comienso-20
			c.setFont('Helvetica',15)
			c.drawString(50,comienso,'Reporte N°: '+str(r.id))
			comienso=comienso-13
			c.setFont('Helvetica',10)
			c.drawString(50,comienso,'date: '+str(r.date))
			comienso=comienso-13
			if(i.unidad == 'Gbl'):
				c.drawString(50,comienso,'alto: '+str(r.alto))
				comienso=comienso-13
			if(i.unidad == 'm2'):
				c.drawString(50,comienso,'alto: '+str(r.alto))
				comienso=comienso-13
				c.drawString(50,comienso,'largo: '+str(r.largo))
				comienso=comienso-13
			if(i.unidad == 'm3'):
				c.drawString(50,comienso,'alto: '+str(r.alto))
				comienso=comienso-13
				c.drawString(50,comienso,'largo: '+str(r.largo))
				comienso=comienso-13
				c.drawString(50,comienso,'ancho: '+str(r.ancho))
				comienso=comienso-13
			c.drawString(50,comienso,'observaciones: '+str(r.observaciones))
			comienso=comienso-13
			
			#if comienso<=300:
			#	print("ya")
			#	c.showPage()
			#	comienso = 750
			
			rf = r.reporte_fotografico_set.all()
			#from django.contrib.sites.models import Site
			for xf in rf:
				from constructora.settings import BASE_DIR
				APP_ROOT = BASE_DIR
				comienso=comienso-155
				c.drawImage(APP_ROOT + xf.fotos_reporte.url,  200,comienso, width=145,height=180, preserveAspectRatio=True)#, anchor='c')
				print("ya")
				
				#if comienso<=200:
				#	c.showPage()
				#	comienso = 750
				
		#c.save()
		c.showPage()
		comienso = 750
	print(comienso)

	# otro
	c.save()
	pdf = buffer.getvalue()
	response.write(pdf)
	return response


def json_calendar(request,pk):
	import json
	dat = []
	query1 = item.objects.filter(proyecto__id=pk)
	for r in query1:
		res = {}
		res['title'] = r.descripcion
		res['start'] = str(r.fecha_inicio)
		res['end'] = str(r.plazo_finalizacion)
		dat.append(res)
	print(dat)
	return HttpResponse(json.dumps(dat), content_type="application/json")
"""