
from rest_framework import viewsets
from .serializers import CarModelSerializer, SonySerializer, \
                        PioneerSerializer
from polimorfismapp.models import CarModel, Sony, Pioneer


class CarModelViewSet(viewsets.ModelViewSet):
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.all()


class SonyViewSet(viewsets.ModelViewSet):
    serializer_class = SonySerializer
    queryset = Sony.objects.all()

class PioneerViewSet(viewsets.ModelViewSet):
    serializer_class = PioneerSerializer
    queryset = Pioneer.objects.all()
