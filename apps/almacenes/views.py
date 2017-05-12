from django.shortcuts import render
from apps.almacenes.forms import *
from apps.almacenes.models import *
from apps.seguimiento.models import *

# Create your views here.

from django.views.generic import ListView, CreateView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, Http404

from easy_pdf.views import PDFTemplateView
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

class crearAlmacen(CreateView):
	form_class = crearAlmacenForm
	template_name = 'almacen/crearalmacen.html'
	success_url = reverse_lazy('almacenes:listaalmacenes')
class actualisarAlmacen(UpdateView):
	model = almacen
	form_class = actualisarAlmacenForm
	template_name = 'almacen/crearalmacen.html'
	success_url = reverse_lazy('almacenes:listaalmacenes')

class listaAlmacenes(CreateView,ListView):
	model = almacen
	form_class = searchForm
	template_name = 'almacen/listaalmacenes.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaAlmacenes, self).get_context_data(**kwargs)	
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
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class crearMaterialAlmacen(CreateView):
	form_class = crearMaterialForm
	template_name = 'almacen/nuevomaterial.html'
	success_url = reverse_lazy('almacenes:listamaterial')

class MaterialUpdate(UpdateView):
	model = material
	form_class = crearMaterialForm
	template_name = 'almacen/nuevomaterial.html'
	success_url = reverse_lazy('almacenes:listamaterial')

class listaMaterial(CreateView,ListView):
	model = material
	form_class = searchForm
	template_name = 'almacen/listamaterial.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaMaterial, self).get_context_data(**kwargs)	
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
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class crearInsumoAlmacen(CreateView):
	form_class = crearInsumoForm
	template_name = 'almacen/nuevoinsumo.html'
	success_url = reverse_lazy('almacenes:listainsumos')

class updateInsumo(UpdateView):
	model = insumos
	form_class = crearInsumoForm
	template_name = 'almacen/nuevoinsumo.html'
	success_url = reverse_lazy('almacenes:listainsumos')

class listaInsumos(CreateView,ListView):
	model = insumos
	form_class = searchForm
	template_name = 'almacen/listainsumos.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaInsumos, self).get_context_data(**kwargs)	
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
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class crearHerramientas(CreateView):
	form_class = crearHerramientasForm
	template_name = 'almacen/nuevaherramienta.html'
	success_url = reverse_lazy('almacenes:listaherramientas')

class updateHerramientas(UpdateView):
	model = herramientas
	form_class = crearHerramientasForm
	template_name = 'almacen/nuevaherramienta.html'
	success_url = reverse_lazy('almacenes:listaherramientas')

class listaHerramientas(CreateView,ListView):
	model = herramientas
	form_class = searchForm
	template_name = 'almacen/listaherramientas.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaHerramientas, self).get_context_data(**kwargs)	
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
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class crearProveedor(CreateView):
	form_class = crearProveedorForm
	template_name = 'almacen/nuevoproveedor.html'
	success_url = reverse_lazy('almacenes:listaproveedor')

class updateProveedor(UpdateView):
	model = proveedor
	form_class = crearProveedorForm
	template_name = 'almacen/nuevaherramienta.html'
	success_url = reverse_lazy('almacenes:listaproveedor')

class listaProveedor(CreateView,ListView):
	model = proveedor
	form_class = searchForm
	template_name = 'almacen/listaproveedor.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaProveedor, self).get_context_data(**kwargs)	
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
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class crearMaquinariaEquipo(CreateView):
	form_class = crearMaquinariaEquipoForm
	template_name = 'almacen/crearmaquinariaequipo.html'
	success_url = reverse_lazy('almacenes:listamaquinariaequipo')

class updateMaquinariaEquipo(UpdateView):
	model = maquinaria_equipo
	form_class = crearMaquinariaEquipoForm
	template_name = 'almacen/nuevaherramienta.html'
	success_url = reverse_lazy('almacenes:listamaquinariaequipo')

class listaMaquinariaEquipo(CreateView,ListView):
	model = maquinaria_equipo
	form_class = searchForm
	template_name = 'almacen/listamaquinariaequipo.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaMaquinariaEquipo, self).get_context_data(**kwargs)	
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
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class listaItemsPedidos(CreateView,ListView):
	model = item
	form_class = searchForm
	template_name = 'almacen/listaitemspedeido.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaItemsPedidos, self).get_context_data(**kwargs)
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
		ct=self.kwargs['ct']
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
			object_list = self.model.objects.filter(proyecto__ubicacion_proyecto=ct,id = id)
		else:
			object_list = self.model.objects.filter(proyecto__ubicacion_proyecto=ct).order_by('id')
		return object_list
# lazys complejos
class ingresoInsumoItem(CreateView):
	model_pk = item
	form_class = crearIngresoInsumoForm
	template_name = 'almacen/crearingresoinsumo.html'
	success_url = 'almacenes:listaingresoinsumo'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.almacen = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
			form.save()
			a=insumosAlmacen.objects.get_or_create(almacen=form.almacen,insumos=form.insumos)
			a[0].cantidad = a[0].cantidad + form.cantidad
			a[0].save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': pk1}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class listaIngresoInsumoItem(CreateView,ListView):
	model = ingresoInsumos
	form_class = searchForm
	template_name = 'almacen/listaingresoinsumoitem.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaIngresoInsumoItem, self).get_context_data(**kwargs)
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
		pk=self.kwargs['pk']
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
			object_list = self.model.objects.filter(item=item.objects.get(id=pk),id = id)
		else:
			object_list = self.model.objects.filter(item=item.objects.get(id=pk)).order_by('id')
		return object_list

class salidaInsumoItem(CreateView):
	model_pk = item
	form_class = crearSalidaInsumoForm
	template_name = 'almacen/salidainsumo.html'
	success_url = 'almacenes:listasalidainsumo'

	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid():
			from django.db.models import Sum
			pk1=self.kwargs['pk']
			#form =form.save(commit=False)
			#almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
			almacen_obj = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
			aux = ingresoInsumos.objects.filter(item=pk1 ,insumos=form.cleaned_data['insumos'],almacen=almacen_obj).aggregate(Sum('cantidad'))
			aux1 = salidaInsumos.objects.filter(item=pk1 ,insumos=form.cleaned_data['insumos'],almacen=almacen_obj).aggregate(Sum('cantidad'))
			total_ing = aux['cantidad__sum']
			#print(total_ing)
			total_sali = aux1['cantidad__sum']
			#print(total_sali)
			if(aux['cantidad__sum'] is None):
				total_ing = 0
			if(aux1['cantidad__sum'] is None):
				total_sali = 0	 
			total = total_ing - total_sali

			if(aux['cantidad__sum'] is None):
				return self.render_to_response(self.get_context_data(form=form,error='No se tiene ingresos de este insumo para el item'))
			if(form.cleaned_data['cantidad']>total):
				return self.render_to_response(self.get_context_data(form=form,error='La cantidad exede el stock actual de '+ str(total)))
			else:
				form =form.save(commit=False)
				#print(almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto))
				form.item = self.model_pk.objects.get(id=pk1)
				form.almacen = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
				form.save()
				a=insumosAlmacen.objects.get(almacen=form.almacen,insumos=form.insumos)
				a.cantidad = a.cantidad - form.cantidad
				a.save()
				return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': pk1}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class listaSalidaInsumo(CreateView,ListView):
	model = salidaInsumos
	form_class = searchForm
	template_name = 'almacen/listasalidainsumo.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaSalidaInsumo, self).get_context_data(**kwargs)
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
		pk=self.kwargs['pk']
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
			object_list = self.model.objects.filter(item=item.objects.get(id=pk),id = id)
		else:
			object_list = self.model.objects.filter(item=item.objects.get(id=pk)).order_by('id')
		return object_list

class ingresoMaterialItem(CreateView):
	model_pk = item
	form_class = crearIngresoMaterialForm
	template_name = 'almacen/crearingresomaterial.html'
	success_url = 'almacenes:listaingresomaterial'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.almacen = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
			form.save()
			a=materialAlmacen.objects.get_or_create(almacen=form.almacen,material=form.material)
			a[0].cantidad = a[0].cantidad + form.cantidad
			a[0].save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': pk1}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class listaIngresoMaterialItem(CreateView,ListView):
	model = ingresoMaterial
	form_class = searchForm
	template_name = 'almacen/listaingresomaterialItem.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaIngresoMaterialItem, self).get_context_data(**kwargs)
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
		pk=self.kwargs['pk']
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
			object_list = self.model.objects.filter(item=item.objects.get(id=pk),id = id)
		else:
			object_list = self.model.objects.filter(item=item.objects.get(id=pk)).order_by('id')
		return object_list

class salidaMaterialItem(CreateView):
	model_pk = item
	form_class = crearSalidaMaterialForm
	template_name = 'almacen/salidamaterial.html'
	success_url = 'almacenes:listasalidamaterial'

	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid():
			from django.db.models import Sum
			pk1=self.kwargs['pk']
			#form =form.save(commit=False)
			#almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)

			almacen_obj = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
			aux = ingresoMaterial.objects.filter(item=pk1 ,material=form.cleaned_data['material'],almacen=almacen_obj).aggregate(Sum('cantidad'))
			aux1 = salidaMaterial.objects.filter(item=pk1 ,material=form.cleaned_data['material'],almacen=almacen_obj).aggregate(Sum('cantidad'))

			total_ing = aux['cantidad__sum']
			#print(total_ing)
			total_sali = aux1['cantidad__sum']
			#print(total_sali)
			if(aux['cantidad__sum'] is None):
				total_ing = 0
			if(aux1['cantidad__sum'] is None):
				total_sali = 0	 
			total = total_ing - total_sali

			if(aux['cantidad__sum'] is None):
				return self.render_to_response(self.get_context_data(form=form,error='No se tiene ingresos de este material para el item'))
			if(form.cleaned_data['cantidad']>total):
				return self.render_to_response(self.get_context_data(form=form,error='La cantidad exede el stock actual de '+ str(total)))
			else:
				form =form.save(commit=False)
				#print(almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto))
				form.item = self.model_pk.objects.get(id=pk1)
				form.almacen = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
				form.save()
				a=materialAlmacen.objects.get(almacen=form.almacen,material=form.material)
				a.cantidad = a.cantidad - form.cantidad
				a.save()
				return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': pk1}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class listaSalidaMaterial(CreateView,ListView):
	model = salidaMaterial
	form_class = searchForm
	template_name = 'almacen/listasalidamaterial.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaSalidaMaterial, self).get_context_data(**kwargs)
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
		pk=self.kwargs['pk']
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
			object_list = self.model.objects.filter(item=item.objects.get(id=pk),id = id)
		else:
			object_list = self.model.objects.filter(item=item.objects.get(id=pk)).order_by('id')
		return object_list

class ingresoHerramientasView(CreateView):
	model_pk = almacen
	form_class = crearIngresoHerramientasForm
	template_name = 'almacen/ingresoherramientas.html'
	success_url = reverse_lazy('almacenes:listaalmacenes')
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid():
			ct=self.kwargs['ct']
			#print(ct)
			form =form.save(commit=False)
			#print(self.model_pk.objects.get(ciudad=ct))
			form.almacen = self.model_pk.objects.get(ciudad=ct)
			form.save()
			a=herramientasAlmacen.objects.get_or_create(almacen=form.almacen,herramientas=form.herramientas)
			a[0].cantidad = a[0].cantidad + form.cantidad
			a[0].save()

			return  HttpResponseRedirect(self.success_url)
		else:
			return self.render_to_response(self.get_context_data(form=form))

class salidaHerramientasView(CreateView):
	model_pk = item
	form_class = crearSalidaHerramientasForm
	template_name = 'almacen/salidaherramientas.html'
	success_url = 'almacenes:listasalidaherramientas'

	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid():
			from django.db.models import Sum
			pk1=self.kwargs['pk']
			#form =form.save(commit=False)
			#almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)

			almacen_obj = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
			aux = ingresoHerramientas.objects.filter(herramientas=form.cleaned_data['herramientas'],almacen=almacen_obj).aggregate(Sum('cantidad'))
			aux1 = salidaHerramientas.objects.filter(herramientas=form.cleaned_data['herramientas'],almacen=almacen_obj,debuelto=False).aggregate(Sum('cantidad'))

			total_ing = aux['cantidad__sum']
			#print(total_ing)
			total_sali = aux1['cantidad__sum']
			#print(total_sali)
			
			if(aux['cantidad__sum'] is None):
				total_ing = 0
			if(aux1['cantidad__sum'] is None):
				total_sali = 0	 
			total = total_ing - total_sali
			print(total)
			"""
			if(aux['cantidad__sum'] is None):
				return self.render_to_response(self.get_context_data(form=form,error='No se tiene ingresos de este herramientas para el item'))
			"""
			if(form.cleaned_data['cantidad']>total):
				return self.render_to_response(self.get_context_data(form=form,error='La cantidad exede el stock actual de '+ str(total)))

			else:
				form =form.save(commit=False)
				#print(almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto))
				form.item = self.model_pk.objects.get(id=pk1)
				form.almacen = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
				form.save()
				a=herramientasAlmacen.objects.get(almacen=form.almacen,herramientas=form.herramientas)
				a.cantidad = a.cantidad - form.cantidad
				a.save()
			
				return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': pk1}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class listaSalidaHerramientas(CreateView,ListView):
	model = salidaHerramientas
	form_class = searchForm
	template_name = 'almacen/listasalidaherramientas.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaSalidaHerramientas, self).get_context_data(**kwargs)
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
		pk=self.kwargs['pk']
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
			object_list = self.model.objects.filter(item=item.objects.get(id=pk),id = id)
		else:
			object_list = self.model.objects.filter(item=item.objects.get(id=pk)).order_by('id')
		return object_list

class ingresoMaquinariaEquipo(CreateView):
	model_pk = almacen
	form_class = crearIngresoMaquinariaEquipoForm
	template_name = 'almacen/ingresomaquinariaequipo.html'
	success_url = reverse_lazy('almacenes:listaalmacenes')
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid():
			ct=self.kwargs['ct']
			#print(ct)
			form =form.save(commit=False)
			#print(self.model_pk.objects.get(ciudad=ct))
			form.almacen = self.model_pk.objects.get(ciudad=ct)
			form.save()
			a=maquinaria_equipoAlmacen.objects.get_or_create(almacen=form.almacen,maquinaria_equipo=form.maquinaria_equipo)
			a[0].cantidad = a[0].cantidad + form.cantidad
			a[0].save()

			return  HttpResponseRedirect(self.success_url)
		else:
			return self.render_to_response(self.get_context_data(form=form))

class salidaMaquinariaEquipo(CreateView):
	model_pk = item
	form_class = crearSalidaMaquinariaEquipoForm
	template_name = 'almacen/salidamaquinariaequipo.html'
	success_url = 'almacenes:listasalidamaquinariaequipo'

	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid():
			from django.db.models import Sum
			pk1=self.kwargs['pk']
			#form =form.save(commit=False)
			#almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)

			almacen_obj = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
			aux = ingresoMaquinaria_equipo.objects.filter(maquinaria_equipo=form.cleaned_data['maquinaria_equipo'],almacen=almacen_obj).aggregate(Sum('cantidad'))
			aux1 = salidaMaquinaria_equipo.objects.filter(maquinaria_equipo=form.cleaned_data['maquinaria_equipo'],almacen=almacen_obj,debuelto=False).aggregate(Sum('cantidad'))

			total_ing = aux['cantidad__sum']
			#print(total_ing)
			total_sali = aux1['cantidad__sum']
			#print(total_sali)
			
			if(aux['cantidad__sum'] is None):
				total_ing = 0
			if(aux1['cantidad__sum'] is None):
				total_sali = 0	 
			total = total_ing - total_sali
			#print(total)
			"""
			if(aux['cantidad__sum'] is None):
				return self.render_to_response(self.get_context_data(form=form,error='No se tiene ingresos de este herramientas para el item'))
			"""
			if(form.cleaned_data['cantidad']>total):
				return self.render_to_response(self.get_context_data(form=form,error='La cantidad exede el stock actual de '+ str(total)))

			else:
				form =form.save(commit=False)
				#print(almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto))
				form.item = self.model_pk.objects.get(id=pk1)
				form.almacen = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
				form.save()
				a=maquinaria_equipoAlmacen.objects.get(almacen=form.almacen,maquinaria_equipo=form.maquinaria_equipo)
				a.cantidad = a.cantidad - form.cantidad
				a.save()
			
				return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': pk1}))

		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class listaSalidaMaquinariaEquipo(CreateView,ListView):
	model = salidaMaquinaria_equipo
	form_class = searchForm
	template_name = 'almacen/listasalidamaquinariaequipo.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaSalidaMaquinariaEquipo, self).get_context_data(**kwargs)
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
		pk=self.kwargs['pk']
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
			object_list = self.model.objects.filter(item=item.objects.get(id=pk),id = id)
		else:
			object_list = self.model.objects.filter(item=item.objects.get(id=pk)).order_by('id')
		return object_list

class listaConfirmacionHerramientas(CreateView,ListView):
	model = salidaHerramientas
	form_class = searchForm
	template_name = 'almacen/listaConfirmacionHerramientas.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaConfirmacionHerramientas, self).get_context_data(**kwargs)
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
		ct=self.kwargs['ct']
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
			object_list = self.model.objects.filter(item__proyecto__ubicacion_proyecto=ct, debuelto=False, id = id)
		else:
			object_list = self.model.objects.filter(item__proyecto__ubicacion_proyecto=ct, debuelto=False).order_by('id')
		return object_list

class debolucionHerramientas(UpdateView):
	model = salidaHerramientas
	form_class = crearDebolucionHerramientas
	template_name = 'almacen/nuevaherramienta_dev.html'
	success_url = 'almacenes:listaconfirmacionherramientas'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		pk = self.kwargs.get('pk',0)
		modelRes = self.model.objects.get(id=pk)

		form = self.form_class(request.POST,instance=modelRes)

		if form.is_valid():
			print (form)
			form =form.save(commit=False)
			if(form.debuelto):

				a = herramientasAlmacen.objects.get(almacen=form.almacen,herramientas=form.herramientas)
				
				ct = a.almacen.ciudad
				
				a.cantidad = a.cantidad + form.cantidad
				a.save()
				form.save()
				print (a)
				print ("paso")
				
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'ct': ct}))
		else:
			print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class listaConfirmacionMaquinariaHequipo(CreateView,ListView):
	model = salidaMaquinaria_equipo
	form_class = searchForm
	template_name = 'almacen/listaConfirmacionMaquinariaHequipo.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaConfirmacionMaquinariaHequipo, self).get_context_data(**kwargs)
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
		ct=self.kwargs['ct']
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
			object_list = self.model.objects.filter(item__proyecto__ubicacion_proyecto=ct, debuelto=False, id = id)
		else:
			object_list = self.model.objects.filter(item__proyecto__ubicacion_proyecto=ct, debuelto=False).order_by('id')
		return object_list

class debolucionMaquinariaHequipo(UpdateView):
	model = salidaMaquinaria_equipo
	form_class = crearDebolucionMaquinariaEquipo
	template_name = 'almacen/nuevamaquinaria_dev.html'
	success_url = 'almacenes:listaconfirmacionmaquinariahequipo'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		pk = self.kwargs.get('pk',0)
		modelRes = self.model.objects.get(id=pk)

		form = self.form_class(request.POST,instance=modelRes)

		if form.is_valid():
			print (form)
			form =form.save(commit=False)
			if(form.debuelto):

				a = maquinaria_equipoAlmacen.objects.get(almacen=form.almacen,maquinaria_equipo=form.maquinaria_equipo)
				ct = a.almacen.ciudad

				a.cantidad = a.cantidad + form.cantidad
				a.save()
				form.save()
				print (a)
				#print ("paso")
			
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'ct': ct}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class crearTipoActivo(CreateView):
	form_class = crearTipoActivoForm
	template_name ='almacen/creartipoactivo.html'
	success_url = "/"
	
class crearActivo(CreateView):
	form_class = crearActivoForm
	template_name ='almacen/crearactivo.html'
	success_url = reverse_lazy('almacenes:listacrearactivo')

class listaCrearActivo(CreateView,ListView):
	model = activo
	form_class = searchForm
	template_name = 'almacen/listaactivo.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaCrearActivo, self).get_context_data(**kwargs)
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
		#ct=self.kwargs['ct']
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
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class crearActivoDepreciasion(CreateView):
	form_class = crearActivoForm
	template_name ='almacen/crearactivodepre.html'
	success_url = "/"
	def get_context_data(self, **kwargs):
		context = super (crearActivoDepreciasion, self).get_context_data(**kwargs)
		import datetime
		datenow = datetime.datetime.now()

		pk=self.kwargs['pk']
		a = activo.objects.get(id=pk)

		act = datenow.year - a.fecha_ingreso.year
		dep = a.costo_total / a.tipoActivo.años_vida_util

		tdep = dep*act
		res= a.costo_total-tdep

		if 'form' not in context or 'res' not in context:
			context['form'] = self.form_class()
			context['res'] = res
		return context


class reporteAlmacen(PDFTemplateView):
	template_name = "almacen/almacenes_reporte.html"
	def get_context_data(self, **kwargs):
		context = super(reporteAlmacen, self).get_context_data(**kwargs)
		pk = self.kwargs.get('ct')
		try:
			context['res'] = almacen.objects.get(ciudad=pk)
		except:
			raise Http404
		return context

class reporteActivo(PDFTemplateView):
	template_name = "almacen/activo_reporte.html"
	def get_context_data(self, **kwargs):
		context = super(reporteActivo, self).get_context_data(**kwargs)
		try:
			context['res'] = activo.objects.all()
		except:
			raise Http404
		return context

class envio_reporte_material(PDFTemplateView):
	template_name = "almacen/envio_reporte_material.html"
	def get_context_data(self, **kwargs):
		context = super(envio_reporte_material, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk')
		try:
			context['res'] = salidaMaterial.objects.get(pk=pk)
			context['usuario'] = self.request.user
		except:
			raise Http404
		return context
class envio_reporte_insumo(PDFTemplateView):
	template_name = "almacen/envio_reporte_insumo.html"
	def get_context_data(self, **kwargs):
		context = super(envio_reporte_insumo, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk')
		try:
			context['res'] = salidaInsumos.objects.get(pk=pk)
			context['usuario'] = self.request.user
		except:
			raise Http404
		return context
"""
def reporteAlmacen(request,ct):
	#consultas

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
	c.drawCentredString(y/2,comienso,'Reporte de Almacen')

	#items

	c.save()
	pdf = buffer.getvalue()
	response.write(pdf)
	return response
"""