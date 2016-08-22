from django.shortcuts import render
#from django.contrib.auth.forms import AuthenticationForm

from django.views.generic.edit import FormMixin
from django.http import Http404
from django.utils.translation import ugettext as _

from django.views.generic import ListView, CreateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from apps.personal.forms import *
from apps.personal.models import *
from django.contrib.auth.models import User

# Create your views here.
def main_page(request):
	return render (request,"base/index.html",{})

class crearUsuario(CreateView):
	model = kardex
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

# clase nueva sobreescrita para busqueda

class FormListView1(FormMixin, ListView):
	def get(self, request, *args, **kwargs):
		# From ProcessFormMixin
		form_class = self.get_form_class()
		self.form = self.get_form(form_class)
		
		# From BaseListView
		self.object_list = self.get_queryset()
		allow_empty = self.get_allow_empty()
		if not allow_empty and len(self.object_list) == 0:
			raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")% {'class_name': self.__class__.__name__})

		context = self.get_context_data(object_list=self.object_list, form=self.form)
		return self.render_to_response(context)

	def post(self, request, *args, **kwargs):
		return self.get(request, *args, **kwargs)
	def form_invalid(self, request, *args, **kwargs):
		return self.get(self, request, *args, **kwargs)

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
		"""
		form = form_class(self.request.GET)
		if form.is_valid():
			object_list = self.model.objects.filter(id = form.cleaned_data['search'], is_staff=False)
		else:
			object_list = self.model.objects.all().filter(is_staff=False).order_by('id')
		return object_list
		"""
		
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