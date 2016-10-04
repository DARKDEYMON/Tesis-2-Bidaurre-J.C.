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

from apps.almacenes.views import *


urlpatterns = [
    url(r'^nuevomaterial/$',
    	login_required(crearMaterialAlmacen.as_view()), 
    	name='nuevomaterial'
    ),
    url(r'^nuevoproveedor/$',
    	login_required(crearProveedor.as_view()), 
    	name='nuevoproveedor'
    ),
    url(r'^crearalmacen/$',
    	login_required(crearAlmacen.as_view()), 
    	name='crearalmacen'
    ),
    url(r'^listaalmacenes/$',
        login_required(listaAlmacenes.as_view()), 
        name='listaalmacenes'
    ),
    url(r'^actualisarAlmacen/(?P<pk>\d+)/$',
        login_required(actualisarAlmacen.as_view()), 
        name='actualisarAlmacen'
    ),
    url(r'^crearherramientas/$',
        login_required(crearHerramientas.as_view()), 
        name='crearherramientas'
    ),
    url(r'^listaitems/(?P<ct>\w+)/$',
        login_required(listaItemsPedidos.as_view()), 
        name='listaitems'
    ),
    url(r'^ingresoinsumo/(?P<pk>\d+)/$',
        login_required(ingresoInsumoItem.as_view()), 
        name='ingresoinsumo'
    ),
    url(r'^salidainsumo/(?P<pk>\d+)/$',
        login_required(salidaInsumoItem.as_view()), 
        name='salidainsumo'
    ),
]