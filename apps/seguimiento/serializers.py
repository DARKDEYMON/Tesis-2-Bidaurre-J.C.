from .models import *
from apps.almacenes.models import *
from rest_framework import serializers

class ItemSerializer(serializers.HyperlinkedModelSerializer):
	#proyecto = serializers.StringRelatedField(many=True)
	proyecto_name = serializers.CharField(source='proyecto.objeto_de_la_contratacion', read_only=True)
	class Meta:
		model = item
		fields = ('id','proyecto_name','descripcion','fecha_inicio', 'plazo_finalizacion', 'unidad','cantidad')

class ReportesSerializer(serializers.HyperlinkedModelSerializer):
	item = serializers.PrimaryKeyRelatedField(read_only=False,queryset=item.objects.all())
	class Meta:
		model = reportes_avance
		fields = ('id','item','date','alto', 'largo', 'ancho','observaciones')

class ReportesFotosSerializer(serializers.HyperlinkedModelSerializer):
	reportes_avance = serializers.PrimaryKeyRelatedField(read_only=False,queryset=reportes_avance.objects.all())
	class Meta:
		model = reporte_fotografico
		fields = ('id','reportes_avance','fotos_reporte')

class RequrimientoMaterialesSerializer(serializers.HyperlinkedModelSerializer):
	item = serializers.PrimaryKeyRelatedField(read_only=False,queryset=item.objects.all())
	material = serializers.PrimaryKeyRelatedField(read_only=False,queryset=material.objects.all())
	class Meta:
		model = peticion_materiales
		fields = ('id','item','material','cantidad','precio_estimado_total','observaciones')

class RequrimientoInsumosSerializer(serializers.HyperlinkedModelSerializer):
	item = serializers.PrimaryKeyRelatedField(read_only=False,queryset=item.objects.all())
	insumos = serializers.PrimaryKeyRelatedField(read_only=False,queryset=insumos.objects.all())
	class Meta:
		model = peticion_insumos
		fields = ('id','item','insumos','cantidad','precio_estimado_total','observaciones')