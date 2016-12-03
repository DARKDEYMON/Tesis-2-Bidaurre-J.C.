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
router.register(r'salidainsumos', salidaInsumosSerializerRest)
router.register(r'salidamaterial', salidaMaterialSerializerRest)

urlpatterns = [
    url(r'^restalmacen/', include(router.urls)),
    url(r'^nuevoproveedor/$',
    	login_required(crearProveedor.as_view()), 
    	name='nuevoproveedor'
    ),
    url(r'^listaproveedor/$',
        login_required(listaProveedor.as_view()), 
        name='listaproveedor'
    ),
    url(r'^updateproveedor/(?P<pk>\d+)/$',
        login_required(updateProveedor.as_view()), 
        name='updateproveedor'
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
    url(r'^listaherramientas/$',
        login_required(listaHerramientas.as_view()), 
        name='listaherramientas'
    ),
    url(r'^updateherramientas/(?P<pk>\d+)/$',
        login_required(updateHerramientas.as_view()), 
        name='updateherramientas'
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
    url(r'^updateinsumo/(?P<pk>\d+)/$',
        login_required(updateInsumo.as_view()), 
        name='updateinsumo'
    ),
    url(r'^listainsumos/$',
        login_required(listaInsumos.as_view()), 
        name='listainsumos'
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
    url(r'^listamaterial/$',
        login_required(listaMaterial.as_view()), 
        name='listamaterial'
    ),
    url(r'^materialupdate/(?P<pk>\d+)/$',
        login_required(MaterialUpdate.as_view()), 
        name='materialupdate'
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
    url(r'^listamaquinariaequipo/$',
        login_required(listaMaquinariaEquipo.as_view()), 
        name='listamaquinariaequipo'
    ),
    url(r'^updatemaquinariaequipo/(?P<pk>\d+)/$',
        login_required(updateMaquinariaEquipo.as_view()), 
        name='updatemaquinariaequipo'
    ),
    url(r'^ingresomaquinariaequipo/(?P<ct>\w+)/$',
        login_required(ingresoMaquinariaEquipo.as_view()), 
        name='ingresomaquinariaequipo'
    ),
    url(r'^salidamaquinariaequipo/(?P<pk>\d+)/$',
        login_required(salidaMaquinariaEquipo.as_view()), 
        name='salidaMaquinariaEquipo'
    ),
    url(r'^listaingresoinsumo/(?P<pk>\d+)/$',
        login_required(listaIngresoInsumoItem.as_view()), 
        name='listaingresoinsumo'
    ),
    url(r'^listaingresomaterial/(?P<pk>\d+)/$',
        login_required(listaIngresoMaterialItem.as_view()), 
        name='listaingresomaterial'
    ),
    url(r'^listasalidamaterial/(?P<pk>\d+)/$',
        login_required(listaSalidaMaterial.as_view()), 
        name='listasalidamaterial'
    ),
    url(r'^listasalidainsumo/(?P<pk>\d+)/$',
        login_required(listaSalidaInsumo.as_view()), 
        name='listasalidainsumo'
    ),
    url(r'^listasalidaherramientas/(?P<pk>\d+)/$',
        login_required(listaSalidaHerramientas.as_view()), 
        name='listasalidaherramientas'
    ),
    url(r'^listasalidamaquinariaequipo/(?P<pk>\d+)/$',
        login_required(listaSalidaMaquinariaEquipo.as_view()), 
        name='listasalidamaquinariaequipo'
    ),
    url(r'^listaconfirmacionherramientas/(?P<ct>\w+)/$',
        login_required(listaConfirmacionHerramientas.as_view()), 
        name='listaconfirmacionherramientas'
    ),
    url(r'^debolucionherramientas/(?P<pk>\d+)/$',
        login_required(debolucionHerramientas.as_view()), 
        name='debolucionherramientas'
    ),

    url(r'^listaconfirmacionmaquinariahequipo/(?P<ct>\w+)/$',
        login_required(listaConfirmacionMaquinariaHequipo.as_view()), 
        name='listaconfirmacionmaquinariahequipo'
    ),
    url(r'^debolucionmaquinariahequipo/(?P<pk>\d+)/$',
        login_required(debolucionMaquinariaHequipo.as_view()), 
        name='debolucionmaquinariahequipo'
    ),
    url(r'^creartipoactivo/$',
        login_required(crearTipoActivo.as_view()), 
        name='creartipoactivo'
    ),
    url(r'^listacrearactivo/$',
        login_required(listaCrearActivo.as_view()), 
        name='listacrearactivo'
    ),
    
    url(r'^crearactivodepreciasion/(?P<pk>\d+)/$',
        login_required(crearActivoDepreciasion.as_view()), 
        name='crearactivodepreciasion'
    ),
    url(r'^crearactivo/$',
        login_required(crearActivo.as_view()), 
        name='crearactivo'
    ),
    url(r'^reportealmacen/(?P<ct>\w+)/$',
        login_required(reporteAlmacen), 
        name='reportealmacen'
    ),
]