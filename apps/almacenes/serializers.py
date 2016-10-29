from apps.seguimiento.models import *
from .models import *
from rest_framework import serializers

class MaterialSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = material
		fields = ('id','decripcion','unidad','observaciones')

class InsumoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = insumos
		fields = ('id','decripcion','unidad','observaciones')

class SalidaInsumosSerializer(serializers.HyperlinkedModelSerializer):
	almacen = serializers.SlugRelatedField(read_only=True, slug_field='ciudad')
	insumos = serializers.SlugRelatedField(read_only=True, slug_field='decripcion')
	item = serializers.SlugRelatedField(read_only=True, slug_field='descripcion')
	cantidad = serializers.IntegerField(read_only=True)
	class Meta:
		model = salidaInsumos
		fields = ('id','almacen','insumos','item','confirmado','fecha','cantidad')

class SalidaMaterialSerializer(serializers.HyperlinkedModelSerializer):
	almacen = serializers.SlugRelatedField(read_only=True, slug_field='ciudad')
	material = serializers.SlugRelatedField(read_only=True, slug_field='decripcion')
	item = serializers.SlugRelatedField(read_only=True, slug_field='descripcion')
	cantidad = serializers.IntegerField(read_only=True)
	class Meta:
		model = salidaMaterial
		fields = ('id','almacen','material','item','confirmado','fecha','cantidad')