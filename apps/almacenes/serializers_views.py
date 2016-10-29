from .models import *
from apps.seguimiento.models import *
from apps.personal.models import *
from rest_framework import viewsets
from .serializers import *

class materialesViewSetRest(viewsets.ModelViewSet):
	model = material
	queryset = material.objects.all()
	serializer_class = MaterialSerializer

class insumosViewSetRest(viewsets.ModelViewSet):
	model = insumos
	queryset = insumos.objects.all()
	serializer_class = InsumoSerializer

class salidaInsumosSerializerRest(viewsets.ModelViewSet):
	model = salidaInsumos
	queryset = salidaInsumos.objects.all()
	serializer_class = SalidaInsumosSerializer
	def get_queryset(self):
		return salidaInsumos.objects.filter(item__proyecto__in=proyecto.objects.filter(designacion__cargo__in=cargo.objects.filter(encargado_de_reportes_avance=True),designacion__user=self.request.user) ,confirmado=False)

class salidaMaterialSerializerRest(viewsets.ModelViewSet):
	model = salidaMaterial
	queryset = salidaMaterial.objects.all()
	serializer_class = SalidaMaterialSerializer
	def get_queryset(self):
		return salidaMaterial.objects.filter(item__proyecto__in=proyecto.objects.filter(designacion__cargo__in=cargo.objects.filter(encargado_de_reportes_avance=True),designacion__user=self.request.user) ,confirmado=False)
