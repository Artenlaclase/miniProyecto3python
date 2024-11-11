from rest_framework import viewsets

from phones.models import Manufacturer, Smartphone
from phones.serializers import ManufacturerSerializer, SmartphoneSerializers

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class SmartphoneViewSet(viewsets.ModelViewSet):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializers

