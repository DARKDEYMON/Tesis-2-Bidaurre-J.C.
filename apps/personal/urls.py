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
from django.conf.urls import url
from django.contrib import admin
from apps.personal.views import *
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #login_required metodo de forsado de login
    url(r'^$', login_required(main_page), name='main'),
    url(r'^nuevousuario/$', login_required(crearUsuario.as_view()), name='nuevousuario'),
    url(r'^listausuario/(?P<id>\d*)/*$', login_required(listaUsuario.as_view()), name='listausuario'),
    #login_required metodo de forsado de login, logout_then_login metodos de logeo de django
    url(r'^login/$',login,{'template_name':'personal/login.html'}, name='login'),
    url(r'^logout/$',logout_then_login, name='logout'),
]