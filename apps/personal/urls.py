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
from apps.personal.views import *
from django.contrib.auth.views import login, logout_then_login, password_reset
from django.contrib.auth.decorators import login_required,permission_required
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import views as auth_views

#rest imports
from rest_framework import routers
from .serializers_views import *

router = routers.DefaultRouter()
router.register(r'currentuser', currentUserViewSetRest)

urlpatterns = [
    #rest routes
    url(r'^restpersonal/', include(router.urls)),
    #login_required metodo de forsado de login
    url(r'^$', 
        login_required(main_page), 
        name='main'
    ),
    url(r'^nuevousuario/$',
        #aqui el decorador de permisos
        permission_required('auth.view_personal')(login_required(crearUsuario.as_view())), 
        name='nuevousuario'
    ),
    #url(r'^listausuario/(?P<id>\d*)/*$', login_required(listaUsuario.as_view()), name='listausuario'),
    url(r'^listausuario/$', 
        login_required(csrf_exempt(listaUsuario.as_view())), 
        name='listausuario'
    ),
    url(r'^updateusuario/(?P<pk>\d+)/$', 
        login_required(updateUsuario.as_view()), 
        name='updateusuario'
    ),
    url(r'^darbaja/(?P<pk>\d+)/$', 
        login_required(updateDarBaja.as_view()), 
        name='updatedarbaja'
    ),
    #actualisacion de cuenta por el usuario
    url(r'^updateusuario_user/$', 
        login_required(updateUsuarioFronUser.as_view()), 
        name='updateusuariofronuser'
    ),
    #login_required metodo de forsado de login, logout_then_login metodos de logeo de django
    url(r'^login/$',
        login,
        {'template_name':'personal/login.html'}, 
        name='login'
    ),
    url(r'^logout/$',
        logout_then_login, 
        name='logout'
    ),
    url(r'^reset_pass/$',
        auth_views.password_change,
        {'template_name':'personal/password_reset_form.html','post_change_redirect' : '/'}, 
        name='reset_password'
    ),
    url(r'^añadirpermisos/(?P<pk>\d+)/$',
        login_required(añadirPermisos.as_view()), 
        name='añadirpermisos'
    ),
    url(r'^crearcargo/$', 
        login_required(crearCargo.as_view()), 
        name='crearcargo'
    ),
    url(r'^listacargo/$', 
        login_required(listaCargo.as_view()), 
        name='listacargo'
    ),
    url(r'^designacion/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_personal')(login_required(crearDesignacion.as_view())), 
        name='designacion'
    ),
    url(r'^listadesignaciones/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_personal')(login_required(listaDesignaciones.as_view())), 
        name='listadesignaciones'
    ),
    url(r'^borrardesig/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_personal')(login_required(borrarDesignacion.as_view())), 
        name='borrardesig'
    ),
    url(r'^updatecargo/(?P<pk>\d+)/$', 
        login_required(updateCargo.as_view()), 
        name='updatecargo'
    ),
]