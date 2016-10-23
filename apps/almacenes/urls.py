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

from rest_framework import routers
from .serializers_views import *

router = routers.DefaultRouter()
router.register(r'materiales', materialesViewSetRest)
router.register(r'insumos', insumosViewSetRest)

urlpatterns = [
    url(r'^restalmacen/', include(router.urls)),
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
    url(r'^ingresoherramientas/(?P<ct>\w+)/$',
        login_required(ingresoHerramientasView.as_view()), 
        name='ingresoherramientas'
    ),
    url(r'^salidaherramientas/(?P<pk>\d+)/$',
        login_required(salidaHerramientasView.as_view()), 
        name='salidaherramientas'
    ),
    url(r'^listaitems/(?P<ct>\w+)/$',
        login_required(listaItemsPedidos.as_view()), 
        name='listaitems'
    ),
    url(r'^crearinsumoalmacen/$',
        login_required(crearInsumoAlmacen.as_view()), 
        name='crearinsumoalmacen'
    ),
    url(r'^ingresoinsumo/(?P<pk>\d+)/$',
        login_required(ingresoInsumoItem.as_view()), 
        name='ingresoinsumo'
    ),
    url(r'^salidainsumo/(?P<pk>\d+)/$',
        login_required(salidaInsumoItem.as_view()), 
        name='salidainsumo'
    ),
    url(r'^nuevomaterial/$',
        login_required(crearMaterialAlmacen.as_view()), 
        name='nuevomaterial'
    ),
    url(r'^ingresomaterial/(?P<pk>\d+)/$',
        login_required(ingresoMaterialItem.as_view()), 
        name='ingresomaterial'
    ),
    url(r'^salidamaterial/(?P<pk>\d+)/$',
        login_required(salidaMaterialItem.as_view()), 
        name='salidamaterial'
    ),
    url(r'^crearmaquinariaequipo/$',
        login_required(crearMaquinariaEquipo.as_view()), 
        name='crearmaquinariaequipo'
    ),
    url(r'^ingresomaquinariaequipo/(?P<ct>\w+)/$',
        login_required(ingresoMaquinariaEquipo.as_view()), 
        name='ingresomaquinariaequipo'
    ),
    url(r'^salidamaquinariaequipo/(?P<pk>\d+)/$',
        login_required(salidaMaquinariaEquipo.as_view()), 
        name='salidaMaquinariaEquipo'
    ),
]