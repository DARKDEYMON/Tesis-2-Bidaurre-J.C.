from django.shortcuts import render
#from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, CreateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from apps.personal.forms import crearUsuarioKardexForm, crearUsuarioUserForm
from apps.personal.models import *

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
		print (form.is_valid())
		print (form2.is_valid())
		if form.is_valid() and form2.is_valid():
			print ("paso")
			form2Save = form2.save(commit=False)
			form2Save.user = form.save()
			form2Save.save()
			return  HttpResponseRedirect(self.succes_url)
		else:
			print ("paso2")
			return self.render_to_response(self.get_context_data(form=form, form2=form2))