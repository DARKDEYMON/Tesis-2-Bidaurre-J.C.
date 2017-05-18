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

#rest imports
from rest_framework import routers
from .serializers_views import *

router = routers.DefaultRouter()
router.register(r'currentitemuser', currentItemViewSetRest)
router.register(r'currentreporte', currentReporteViewSetRest)
router.register(r'currentreportefotos', currentReporteFotosViewSetRest)
router.register(r'peticionmaterial', requrimientoMaterialesSerializerViewSetRest)
router.register(r'peticioninsumo', requrimientoInsumosSerializerViewSetRest)

urlpatterns = [
    url(r'^restseguimiento/', include(router.urls)),
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
    url(r'^updateitem/(?P<pk>\d+)/$',
        login_required(updateItem.as_view()), 
        name='updateitem'
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
    url(r'^listapeticionmaterial/(?P<pk>\d+)/$',
        login_required(csrf_exempt(listaPeticionMaterial.as_view())), 
        name='listapeticionmaterial'
    ),
    url(r'^updatepeticionmaterial/(?P<pk>\d+)/$',
        login_required(updatePeticionMaterial.as_view()), 
        name='updatepeticionmaterial'
    ),
    url(r'^peticioninsumos/(?P<pk>\d+)/$',
        login_required(peticionInsumos.as_view()), 
        name='peticioninsumos'
    ),
    url(r'^listapeticioninsumos/(?P<pk>\d+)/$',
        login_required(csrf_exempt(listaPeticionInsumos.as_view())), 
        name='listapeticioninsumos'
    ),
    url(r'^updatepeticioninsumos/(?P<pk>\d+)/$',
        login_required(updatePeticionInsumos.as_view()), 
        name='updatepeticioninsumos'
    ),
    url(r'^requerimientopersonal/(?P<pk>\d+)/$',
        login_required(requerimientoPersonal.as_view()), 
        name='requerimientopersonal'
    ),
    url(r'^listareqpersonal/(?P<pk>\d+)/$',
        login_required(csrf_exempt(listaRequerimientoPersonal.as_view())), 
        name='listareqpersonal'
    ),
    url(r'^updaterequerimientopersonal/(?P<pk>\d+)/$',
        login_required(updateRequerimientoPersonal.as_view()), 
        name='updaterequerimientopersonal'
    ),
    url(r'^requerimientomahe/(?P<pk>\d+)/$',
        login_required(requerimientoMaHe.as_view()), 
        name='requerimientoMaHe'
    ),
    url(r'^listarequerimientomahe/(?P<pk>\d+)/$',
        login_required(csrf_exempt(listaRequerimientoMaHe.as_view())), 
        name='listarequerimientomahe'
    ),
    url(r'^updaterequerimientomahe/(?P<pk>\d+)/$',
        login_required(updateRequerimientoMaHe.as_view()), 
        name='updaterequerimientomahe'
    ),
    url(r'^requerimientomatlo/(?P<pk>\d+)/$',
        login_required(requerimientoMaterialesLocales.as_view()), 
        name='requerimientomatlo'
    ),
    url(r'^listaRequerimientomalo/(?P<pk>\d+)/$',
        login_required(csrf_exempt(listaRequerimientoMaterialeLocales.as_view())), 
        name='listaRequerimientomalo'
    ),  
    url(r'^updaterequerimientomatlo/(?P<pk>\d+)/$',
        login_required(updateRequerimientoMaterialesLocales.as_view()), 
        name='updaterequerimientomatlo'
    ),
    url(r'^requerimientoherramientas/(?P<pk>\d+)/$',
        login_required(requerimientoHerramientas.as_view()), 
        name='requerimientoherramientas'
    ),
    url(r'^listarequerimientoherr/(?P<pk>\d+)/$',
        login_required(csrf_exempt(listaRequerimientoHerramientas.as_view())), 
        name='listarequerimientoherr'
    ),
    url(r'^updatepeticionherramientas/(?P<pk>\d+)/$',
        login_required(updatePeticionHerramientas.as_view()), 
        name='updatepeticionherramientas'
    ),
    url(r'^crearinforme/(?P<pk>\d+)/$',
        login_required(crearInforme.as_view()), 
        name='crearinforme'
    ),
    url(r'^updatecrearinforme/(?P<pk>\d+)/$',
        login_required(updateCrearInforme.as_view()), 
        name='updatecrearinforme'
    ),
    url(r'^informefotografico/(?P<pk>\d+)/$',
        login_required(crearInformeFotografico.as_view()), 
        name='informefotografico'
    ),
    url(r'^listainformes/(?P<pk>\d+)/$',
        login_required(listaInformes.as_view()), 
        name='listainformes'
    ),
    url(r'^listainformesfotos/(?P<pk>\d+)/$',
        login_required(listaInformesFotos.as_view()), 
        name='listainformesfotos'
    ),
    url(r'^reporteproyecto/(?P<pk>\d+)/$',
        login_required(reporteProyecto.as_view()), 
        name='reporteproyecto'
    ),

    url(r'^calendar/(?P<pk>\d+)/$',
        login_required(calendar_proyecto), 
        name='calendar'
    ),
    url(r'^repestpro/$',
        login_required(reporteProyectosEstado.as_view()), 
        name='repestpro'
    ),
    #url(r'^json_calendar/(?P<pk>\d+)/$',
    #    login_required(json_calendar), 
    #    name='json_calendar'
    #),
]