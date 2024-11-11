from rest_framework import serializers

from phones.models import Manufacturer, Smartphone

class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'country', 'date_founded', 'webpage']


class SmartphoneSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Smartphone
        fields = ['manufacturer', 'name', 'ram_gb', 'storage_gb', 'screen_inches']