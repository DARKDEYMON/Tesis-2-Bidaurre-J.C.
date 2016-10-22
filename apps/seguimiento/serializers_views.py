from .models import *
from apps.personal.models import *
from rest_framework import viewsets
from .serializers import *

class currentItemViewSetRest(viewsets.ModelViewSet):
	model = item
	queryset = item.objects.all()
	serializer_class = ItemSerializer
	
	def get_queryset(self):
		return item.objects.filter(proyecto__in=proyecto.objects.filter(designacion__cargo__in=cargo.objects.filter(encargado_de_reportes_avance=True),designacion__user=self.request.user))

class currentReporteViewSetRest(viewsets.ModelViewSet):
	model = reportes_avance
	queryset = reportes_avance.objects.all()
	serializer_class = ReportesSerializer

class currentReporteFotosViewSetRest(viewsets.ModelViewSet):
	model = reporte_fotografico
	queryset = reporte_fotografico.objects.all()
	serializer_class = ReportesFotosSerializer

class requrimientoMaterialesSerializerViewSetRest(viewsets.ModelViewSet):
	model = peticion_materiales
	queryset = peticion_materiales.objects.all()
	serializer_class = RequrimientoMaterialesSerializer