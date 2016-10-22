from .models import *
from rest_framework import viewsets
from .serializers import *

class materialesViewSetRest(viewsets.ModelViewSet):
	model = material
	queryset = material.objects.all()
	serializer_class = MaterialSerializer