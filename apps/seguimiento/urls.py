"""constructora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required,permission_required
from django.views.decorators.csrf import csrf_exempt

from apps.seguimiento.views import *


urlpatterns = [
    url(r'^nuevoproyecto/$',
        login_required(crearProyecto.as_view()), 
        name='nuevoproyecto'
    ),
    url(r'^listaproyectos/$',
        login_required(csrf_exempt(listaProyectos.as_view())), 
        name='listaproyectos'
    ),
    url(r'^crearitem/(?P<pk>\d+)/$',
        login_required(crearItem.as_view()), 
        name='crearitem'
    ),
    url(r'^listaItems/(?P<pk>\d+)/$',
        login_required(csrf_exempt(listaItems.as_view())), 
        name='listaitems'
    ),
    url(r'^updateproyect/(?P<pk>\d+)/$',
        login_required(updateProyecto.as_view()), 
        name='updateproyect'
    ),
    url(r'^listapersonal/(?P<pk>\d+)/$',
        login_required(listaPersonalProyecto.as_view()), 
        name='listapersonal'
    ),
    url(r'^peticionmaterial/(?P<pk>\d+)/$',
        login_required(peticionMaterial.as_view()), 
        name='peticionmaterial'
    ),
]