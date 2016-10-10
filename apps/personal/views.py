from django.shortcuts import render
#from django.contrib.auth.forms import AuthenticationForm

from django.views.generic.edit import FormMixin
from django.http import Http404
from django.utils.translation import ugettext as _

from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from apps.personal.forms import *
from apps.personal.models import *
from django.contrib.auth.models import User

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Create your views here.
def main_page(request):
	return render (request,"base/index.html",{})

#crea un nuebo usuario
class crearUsuario(CreateView):
	#model = User
	#permission_required = 'auth.view_personal'
	form_class = crearUsuarioUserForm
	second_form_class = crearUsuarioKardexForm
	template_name = 'personal/nuevousuario.html'
	succes_url = reverse_lazy('personal:listausuario')
	def get_context_data(self, **kwargs):
		context = super (crearUsuario, self).get_context_data(**kwargs)
		if 'form' not in context or 'form2' not in context:
			context['form'] = self.form_class()
			context['form2'] = self.second_form_class()
		return context
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST,request.FILES)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid() and form2.is_valid():
			#print ("paso")
			form2Save = form2.save(commit=False)
			form2Save.user = form.save()
			form2Save.save()
			return  HttpResponseRedirect(self.succes_url)
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form, form2=form2))

#actualisa un usuario desde el modulo de personal
class updateUsuario(UpdateView):
	model = User
	second_model = kardex
	form_class = updateUsuarioUserForm
	second_form_class = crearUsuarioKardexForm
	template_name = 'personal/nuevousuario.html'
	succes_url = reverse_lazy('personal:listausuario')
	def get_context_data(self, **kwargs):
		context = super(updateUsuario, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		modelRes = self.model.objects.get(id=pk)
		modelRes2 = self.second_model.objects.get(id=modelRes.id)
		if 'form' not in context or 'form2' not in context:
			context['form'] = self.form_class(instance=modelRes)
			context['form2'] = self.second_form_class(instance=modelRes2)
		return context
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		pk = self.kwargs.get('pk',0)
		modelRes = self.model.objects.get(id=pk)
		modelRes2 = self.second_model.objects.get(id=modelRes.id)

		form = self.form_class(request.POST,instance=modelRes)
		form2 = self.second_form_class(request.POST,request.FILES, instance=modelRes2)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid() and form2.is_valid():
			#print ("paso")
			form2Save = form2.save(commit=False)
			form2Save.user = form.save()
			form2Save.save()
			return  HttpResponseRedirect(self.succes_url)
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form, form2=form2))

#actualisa datos del usuario actual logeado
class updateUsuarioFronUser(UpdateView):
	model = kardex
	form_class = crearModificarKardexForm
	template_name = 'personal/updatefromuser.html'
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super(updateUsuarioFronUser, self).get_context_data(**kwargs)
		pk = self.request.user.id
		print(pk)
		modelRes = self.model.objects.get(id=pk)
		if 'form' not in context:
			context['form'] = self.form_class(instance=modelRes)
		if 'uss' not in context:
			context['uss'] = self.get_object()
		return context

	def get_object(self):
		return self.model.objects.get(user=self.request.user)

#actualisa da un usuario en alta o baja 
class updateDarBaja(UpdateView):
	model = User
	form_class = darBajaForm
	template_name = 'personal/updatefromuser.html'
	success_url = reverse_lazy('personal:listausuario')

#añade o quita permisos de acceso a los diferentes modulos a un usuario en espesifico por el id
class añadirPermisos(FormView):
	model = User
	form_class = addPermissionsFrom
	template_name = 'personal/añadirpermisos.html'
	succes_url = reverse_lazy('personal:listausuario')

	def get_context_data(self, **kwargs):
		context = super(añadirPermisos, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		user = self.model.objects.get(id=pk)
		form = self.form_class(initial={'mod_personal':user.has_perm('auth.view_personal'),
										'mod_seguimiento':user.has_perm('auth.view_seguimiento'),
										'mod_almacenes':user.has_perm('auth.view_almacen')})
		#form.fields["mod_personal"] = True
		#print(form)
		if 'form' in context :
			context['form'] = form
		return context
	def post(self, request, *args, **kwargs):
		#self.object = self.get_object	
		form = self.form_class(request.POST)
		pk = self.kwargs.get('pk',0)
		my_user = self.model.objects.get(id=pk)
		if form.is_valid():
			content_type = ContentType.objects.get_for_model(self.model)
			permission = Permission.objects.get(content_type=content_type, codename='view_personal')
			if(form.cleaned_data['mod_personal']):
				my_user.user_permissions.add(permission)
			else:
				my_user.user_permissions.remove(permission)
			permission = Permission.objects.get(content_type=content_type, codename='view_seguimiento')
			if(form.cleaned_data['mod_seguimiento']):
				my_user.user_permissions.add(permission)
			else:
				my_user.user_permissions.remove(permission)
			permission = Permission.objects.get(content_type=content_type, codename='view_almacen')
			if(form.cleaned_data['mod_almacenes']):
				my_user.user_permissions.add(permission)
			else:
				my_user.user_permissions.remove(permission)

			return  HttpResponseRedirect(self.succes_url)
		else:
			print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

#crea un listado de los usuarios con los diferentes opciones de modificacion y un buscador por id
class listaUsuario(CreateView, ListView):
	model = User
	form_class = searchForm
	template_name='personal/listausuario.html'
	paginate_by = 10

	# aun sin saber si cirve
	def get_context_data(self, **kwargs):
		context = super (listaUsuario, self).get_context_data(**kwargs)
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
			object_list = self.model.objects.filter(id = id, is_staff=False)
		else:
			object_list = self.model.objects.all().filter(is_staff=False).order_by('id')
		return object_list

class crearCargo(CreateView):
	form_class = cargoForm
	template_name = 'personal/nuevocargo.html'
	success_url = '/'

class listaCargo(CreateView,ListView):
	model = cargo
	form_class = searchForm
	template_name = 'personal/listacargo.html'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super (listaCargo, self).get_context_data(**kwargs)
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
			object_list = self.model.objects.filter(pk=id)
		else:
			object_list = self.model.objects.all().filter().order_by('id')
		return object_list

class crearDesignacion(CreateView):
	model = User
	#permission_required = 'auth.view_personal'
	form_class = designacionForm
	#second_form_class = designacion_cargoForm
	template_name = 'personal/designacion.html'
	succes_url = reverse_lazy('personal:listausuario')

	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		pk = self.kwargs.get('pk',0)
		#form.data["user"] =	pk
		#a=designacion.objects.filter(user=User.objects.get(pk=pk),proyecto=proyecto.objects.get(pk=form.cleaned_data['proyecto']))
		#form2 = self.second_form_class(request.POST)
		if form.is_valid():
			#print (form.cleaned_data['proyecto'].pk)
			#verifica si el usuarioya tiene un cargo designado en el proyecto
			#print(len(designacion.objects.filter(cargo=form.cleaned_data['cargo'],proyecto=form.cleaned_data['proyecto'])))
			#print(designacion.objects.filter(cargo=form.cleaned_data['cargo'],proyecto=form.cleaned_data['proyecto']))
			if(len(designacion.objects.filter(user=User.objects.get(pk=pk),proyecto=form.cleaned_data['proyecto']))!=0 or len(designacion.objects.filter(cargo=form.cleaned_data['cargo'],proyecto=form.cleaned_data['proyecto']))!=0):
				if(len(designacion.objects.filter(user=User.objects.get(pk=pk),proyecto=form.cleaned_data['proyecto']))!=0):
					return self.render_to_response(self.get_context_data(form=form,error='El usuario ya tiene una asignacion de cargo en este proyecto'))
				if(len(designacion.objects.filter(cargo=form.cleaned_data['cargo'],proyecto=form.cleaned_data['proyecto']))!=0):
					return self.render_to_response(self.get_context_data(form=form,error='El cargo ya esta asignado a una persona en el proyecto'))
			else:
				form1Save = form.save(commit=False)
				form1Save.user = self.model.objects.get(id=pk)
				form.save()
				return  HttpResponseRedirect(self.succes_url)
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class listaDesignaciones(CreateView, ListView):
	model = designacion
	form_class = searchForm
	template_name='personal/listadesignacion.html'
	paginate_by = 10

	# aun sin saber si cirve
	def get_context_data(self, **kwargs):
		context = super (listaDesignaciones, self).get_context_data(**kwargs)
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
			object_list = self.model.objects.filter(pk=id, user=User.objects.filter(pk=pk), is_staff=False)
		else:
			object_list = self.model.objects.all().filter(user=User.objects.filter(pk=pk)).order_by('id')
		return object_list
class borrarDesignacion(DeleteView):
	model = designacion
	template_name ='personal/borrardesignacion.html'
	success_url = 'personal:listadesignaciones'
	def get_success_url(self, **kwargs):
		return reverse_lazy(self.success_url, kwargs = {'pk': self.get_object().user.pk})

"""class updateDesignacion(UpdateView):
	model = designacion
	form_class = designacionForm
	template_name = 'personal/updatefromuser.html'
	success_url = 'personal:listadesignaciones'

	def get_context_data(self, **kwargs):
		context = super(updateDesignacion, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		modelRes = self.model.objects.get(id=pk)
		if 'form' in context:
			context['form'] = self.form_class(instance=modelRes)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		pk = self.kwargs.get('pk',0)
		#form.data["user"] =	pk
		#a=designacion.objects.filter(user=User.objects.get(pk=pk),proyecto=proyecto.objects.get(pk=form.cleaned_data['proyecto']))
		#form2 = self.second_form_class(request.POST)
		if form.is_valid():
			#print (form.cleaned_data['proyecto'].pk)
			#verifica si el usuarioya tiene un cargo designado en el proyecto
			#print(len(designacion.objects.filter(cargo=form.cleaned_data['cargo'],proyecto=form.cleaned_data['proyecto'])))
			#print(designacion.objects.filter(cargo=form.cleaned_data['cargo'],proyecto=form.cleaned_data['proyecto']))
			if(len(designacion.objects.filter(user=User.objects.get(pk=pk),proyecto=form.cleaned_data['proyecto']))!=0 or len(designacion.objects.filter(cargo=form.cleaned_data['cargo'],proyecto=form.cleaned_data['proyecto']))!=0):
				if(len(designacion.objects.filter(user=User.objects.get(pk=pk),proyecto=form.cleaned_data['proyecto']))!=0):
					return self.render_to_response(self.get_context_data(form=form,error='El usuario ya tiene una asignacion de cargo en este proyecto'))
				if(len(designacion.objects.filter(cargo=form.cleaned_data['cargo'],proyecto=form.cleaned_data['proyecto']))!=0):
					return self.render_to_response(self.get_context_data(form=form,error='El cargo ya esta asignado a una persona en el proyecto'))
			else:
				form1Save = form.save(commit=False)
				form1Save.user = self.model.objects.get(id=pk)
				for_rever = form.save()
				return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs={'pk': for_rever.pk}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))"""


class updateCargo(UpdateView):
	model = cargo
	form_class = cargoForm
	template_name = 'personal/nuevocargo.html'
	success_url = reverse_lazy('personal:listacargo')