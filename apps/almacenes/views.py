from django.shortcuts import render
from apps.almacenes.forms import *
from apps.almacenes.models import *
from apps.seguimiento.models import *

# Create your views here.

from django.views.generic import ListView, CreateView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

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
	success_url = '/'

class crearInsumoAlmacen(CreateView):
	form_class = crearInsumoForm
	template_name = 'almacen/nuevoinsumo.html'
	success_url = '/'

class crearHerramientas(CreateView):
	form_class = crearHerramientasForm
	template_name = 'almacen/nuevaherramienta.html'
	success_url = '/'

class crearProveedor(CreateView):
	form_class = crearProveedorForm
	template_name = 'almacen/nuevoproveedor.html'
	success_url = '/'

class crearMaquinariaEquipo(CreateView):
	form_class = crearMaquinariaEquipoForm
	template_name = 'almacen/crearmaquinariaequipo.html'
	success_url = '/'

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

class ingresoInsumoItem(CreateView):
	model_pk = item
	form_class = crearIngresoInsumoForm
	template_name = 'almacen/crearingresoinsumo.html'
	success_url = '/'
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
			return  HttpResponseRedirect(self.success_url)
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class salidaInsumoItem(CreateView):
	model_pk = item
	form_class = crearSalidaInsumoForm
	template_name = 'almacen/salidainsumo.html'
	success_url = '/'

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
				return  HttpResponseRedirect(self.success_url)
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class ingresoMaterialItem(CreateView):
	model_pk = item
	form_class = crearIngresoMaterialForm
	template_name = 'almacen/crearingresomaterial.html'
	success_url = '/'
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
			return  HttpResponseRedirect(self.success_url)
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class salidaMaterialItem(CreateView):
	model_pk = item
	form_class = crearSalidaMaterialForm
	template_name = 'almacen/salidamaterial.html'
	success_url = '/'

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
				return  HttpResponseRedirect(self.success_url)
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

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
	success_url = '/'

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
			aux1 = salidaHerramientas.objects.filter(herramientas=form.cleaned_data['herramientas'],almacen=almacen_obj).aggregate(Sum('cantidad'))

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
			
				return  HttpResponseRedirect(self.success_url)

		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))


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
	success_url = '/'

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
			aux1 = salidaMaquinaria_equipo.objects.filter(maquinaria_equipo=form.cleaned_data['maquinaria_equipo'],almacen=almacen_obj).aggregate(Sum('cantidad'))

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
			
				return  HttpResponseRedirect(self.success_url)

		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))