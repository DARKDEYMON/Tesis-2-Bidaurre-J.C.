from django.shortcuts import render
#from django.contrib.auth.forms import AuthenticationForm

from django.views.generic.edit import FormMixin
from django.http import Http404
from django.utils.translation import ugettext as _

from django.views.generic import ListView, CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from apps.personal.forms import *
from apps.personal.models import *
from django.contrib.auth.models import User

# Create your views here.
def main_page(request):
	return render (request,"base/index.html",{})

class crearUsuario(CreateView):
	#model = User
	form_class = crearUsuarioUserForm
	second_form_class = crearUsuarioKardexForm
	template_name = 'personal/nuevousuario.html'
	succes_url = '/'
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

class updateUsuario(UpdateView):
	model = User
	second_model = kardex
	form_class = crearUsuarioUserForm
	second_form_class = crearUsuarioKardexForm
	template_name = 'personal/nuevousuario.html'
	succes_url = '/'
	def get_context_data(self, **kwargs):
		context = super(updateUsuario, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		modelRes = self.model.objects.get(id=pk)
		modelRes2 = self.second_model.objects.get(id=modelRes.id)
		if 'form' not in context or 'form2' not in context:
			context['form'] = self.form_class(instance=modelRes)
			context['form2'] = self.second_form_class(instance=modelRes2)
		return context

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