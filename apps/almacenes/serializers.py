from .models import *
from rest_framework import serializers

class MaterialSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = material
		fields = ('id','decripcion','unidad','observaciones')