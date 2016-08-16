from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def main_page(request):
	return render (request,"base/index.html",{})