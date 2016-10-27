from .models import *
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