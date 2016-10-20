from .models import *
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
		fields = ('id','item','date','alto', 'largo', 'ancho')